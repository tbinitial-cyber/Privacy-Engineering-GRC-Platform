import asyncio
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\europe_audit")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TRACKER_DOMAINS = [
    "clarity.ms",
    "tapad.com",
    "google-analytics.com",
    "googletagmanager.com",
    "doubleclick.net",
    "facebook.com",
    "facebook.net",
    "linkedin.com",
    "licdn.com",
    "bing.com",
    "bat.bing.com",
    "ads-twitter.com",
    "hotjar.com",
    "segment.io",
    "segment.com",
    "datadoghq-browser-agent.com",
    "onetrust.com",
    "cookielaw.org"
]

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def identify_tracker(url):
    for domain in TRACKER_DOMAINS:
        if domain in url:
            return domain
    return None

async def run_audit():
    print("=" * 60)
    print("STARTING MIRO EUROPEAN UNION (FRANCE) GDPR AUDIT")
    print("=" * 60)
    
    proxy_server = "http://127.0.0.1:61809"
    results = {
        "audit_timestamp": now_iso(),
        "proxy_used": proxy_server,
        "geoip_verification": {},
        "pre_consent": {
            "banner_detected": False,
            "banner_text": "",
            "buttons_found": {},
            "cookies": [],
            "cookie_count": 0,
            "requests_count": 0,
            "tracker_requests": [],
            "onetrust_active_groups": None,
            "optanon_consent_cookie": None
        },
        "post_reject": {},
        "post_accept": {}
    }

    async with async_playwright() as p:
        print(f"[1/6] Launching Chromium with proxy {proxy_server}...")
        browser = await p.chromium.launch(
            headless=True,
            proxy={"server": proxy_server}
        )

        # 1. GeoIP verification via OneTrust endpoint
        print("[2/6] Verifying browser-level GeoIP recognition from OneTrust endpoint...")
        geo_context = await browser.new_context()
        geo_page = await geo_context.new_page()
        try:
            resp = await geo_page.goto("https://geolocation.onetrust.com/cookieconsentpub/v1/geo/location", timeout=20000)
            text = await resp.text()
            print(f"      GeoIP Response: {text.strip()}")
            match = re.search(r'jsonFeed\((.*)\);', text)
            if match:
                results["geoip_verification"] = json.loads(match.group(1))
            else:
                results["geoip_verification"] = {"raw": text}
        except Exception as e:
            print(f"      GeoIP check error: {e}")
            results["geoip_verification"] = {"error": str(e)}
        finally:
            await geo_context.close()

        # 2. Pre-Consent Capture on Miro
        print("[3/6] Creating clean session and navigating to https://miro.com ...")
        context = await browser.new_context(
            viewport={"width": 1366, "height": 768},
            locale="fr-FR",
            timezone_id="Europe/Paris"
        )
        page = await context.new_page()

        requests_logged = []
        trackers_fired_pre_consent = []

        async def on_request(req):
            tracker = identify_tracker(req.url)
            req_info = {
                "url": req.url,
                "method": req.method,
                "resource_type": req.resource_type,
                "tracker": tracker,
                "timestamp": now_iso()
            }
            requests_logged.append(req_info)
            if tracker:
                trackers_fired_pre_consent.append(req_info)

        page.on("request", on_request)

        try:
            await page.goto("https://miro.com", wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"      Navigation notice: {e}, waiting 5s for settling...")
            await page.wait_for_timeout(5000)

        await page.wait_for_timeout(3000)

        # Inspect OneTrust banner
        print("[4/6] Inspecting OneTrust Consent Banner in France...")
        banner = page.locator("#onetrust-banner-sdk")
        banner_present = await banner.is_visible()
        results["pre_consent"]["banner_detected"] = banner_present
        print(f"      OneTrust Banner Visible: {banner_present}")

        if banner_present:
            banner_text = await banner.inner_text()
            results["pre_consent"]["banner_text"] = banner_text
            print(f"      Banner Text Snippet:\n      {banner_text[:200]}...")

        # Detect specific buttons
        buttons = {
            "accept_all": "#onetrust-accept-btn-handler",
            "reject_all": "#onetrust-reject-all-handler",
            "cookie_settings": "#onetrust-pc-btn-handler",
            "close_btn": "#onetrust-close-btn-container"
        }
        for b_name, selector in buttons.items():
            btn = page.locator(selector)
            vis = await btn.is_visible()
            results["pre_consent"]["buttons_found"][b_name] = {
                "selector": selector,
                "visible": vis,
                "text": (await btn.inner_text()).strip() if vis else None
            }
            print(f"      Button '{b_name}' ({selector}): Visible={vis}")

        # Capture Pre-Consent Cookies
        cookies_pre = await context.cookies()
        results["pre_consent"]["cookies"] = cookies_pre
        results["pre_consent"]["cookie_count"] = len(cookies_pre)
        results["pre_consent"]["requests_count"] = len(requests_logged)
        results["pre_consent"]["tracker_requests"] = trackers_fired_pre_consent

        # Check Optanon / OneTrust cookies
        for c in cookies_pre:
            if c["name"] == "OptanonConsent":
                results["pre_consent"]["optanon_consent_cookie"] = c["value"]
            elif c["name"] == "OptanonAlertBoxClosed":
                results["pre_consent"]["optanon_alert_box_closed"] = c["value"]

        # Check Active Groups from DOM
        try:
            active_groups = await page.evaluate("() => window.OnetrustActiveGroups || null")
            results["pre_consent"]["onetrust_active_groups"] = active_groups
        except Exception:
            pass

        # Pre-consent screenshot
        pre_shot = OUTPUT_DIR / "europe_pre_consent.png"
        await page.screenshot(path=str(pre_shot), full_page=False)
        print(f"      Saved screenshot: {pre_shot.name}")

        # Save HTML
        pre_html = await page.content()
        (OUTPUT_DIR / "europe_pre_consent.html").write_text(pre_html, encoding="utf-8")

        print(f"      [PRE-CONSENT TOTALS]")
        print(f"      Cookies dropped: {len(cookies_pre)}")
        print(f"      Trackers fired: {len(trackers_fired_pre_consent)}")
        for t in trackers_fired_pre_consent[:10]:
            print(f"        -> {t['tracker']}: {t['url'][:80]}")

        # 3. Test "Reject All" if available, or "Cookie Settings"
        print("[5/6] Testing Consent Action under EU rules...")
        reject_btn = page.locator("#onetrust-reject-all-handler")
        has_reject = await reject_btn.is_visible()

        if has_reject:
            print("      Clicking 'Reject All' (#onetrust-reject-all-handler)...")
            requests_logged.clear()
            await reject_btn.click()
            await page.wait_for_timeout(4000)
            
            post_reject_cookies = await context.cookies()
            results["post_reject"] = {
                "action": "Clicked Reject All",
                "cookie_count": len(post_reject_cookies),
                "cookies": post_reject_cookies,
                "new_requests_count": len(requests_logged),
                "new_tracker_requests": [r for r in requests_logged if r["tracker"] is not None]
            }
            try:
                results["post_reject"]["onetrust_active_groups"] = await page.evaluate("() => window.OnetrustActiveGroups || null")
            except Exception:
                pass
            reject_shot = OUTPUT_DIR / "europe_post_reject.png"
            await page.screenshot(path=str(reject_shot), full_page=False)
            print(f"      Saved post-reject screenshot: {reject_shot.name}")
        else:
            print("      [FINDING] 'Reject All' button (#onetrust-reject-all-handler) is NOT visible on banner!")
            results["post_reject"] = {
                "action": "Reject All button absent",
                "finding": "Lack of equal prominence for Reject button under GDPR Art. 7(3) and CNIL/EDPB guidelines."
            }

        # 4. Save Final Report
        report_json = OUTPUT_DIR / "miro_europe_telemetry.json"
        with open(report_json, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)

        print("[6/6] European Audit Complete! Output saved to:")
        print(f"      {report_json}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_audit())
