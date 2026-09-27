import asyncio
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\freshworks_audit")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TRACKER_DOMAINS = [
    "google-analytics.com",
    "googletagmanager.com",
    "doubleclick.net",
    "clarity.ms",
    "tapad.com",
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
    "cookielaw.org",
    "marketo.net",
    "bizible.com",
    "demandbase.com",
    "quora.com",
    "reddit.com"
]

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def identify_tracker(url):
    for domain in TRACKER_DOMAINS:
        if domain in url:
            return domain
    return None

async def audit_session(p, session_name, proxy_config):
    print(f"\n--- AUDITING FRESHWORKS ({session_name}) ---")
    results = {
        "session": session_name,
        "timestamp": now_iso(),
        "proxy": proxy_config.get("server") if proxy_config else "Direct (No Proxy)",
        "pre_consent": {
            "banner_detected": False,
            "banner_type": None,
            "banner_text": "",
            "buttons_found": {},
            "cookie_count": 0,
            "cookies": [],
            "requests_count": 0,
            "tracker_requests": []
        }
    }

    launch_args = {"headless": True}
    if proxy_config:
        launch_args["proxy"] = proxy_config

    browser = await p.chromium.launch(**launch_args)
    ctx = await browser.new_context(
        viewport={"width": 1366, "height": 768},
        locale="fr-FR" if proxy_config else "en-IN",
        timezone_id="Europe/Paris" if proxy_config else "Asia/Kolkata"
    )
    page = await ctx.new_page()

    requests_logged = []
    trackers_logged = []

    async def on_request(req):
        t = identify_tracker(req.url)
        item = {
            "url": req.url,
            "method": req.method,
            "resource_type": req.resource_type,
            "tracker": t,
            "timestamp": now_iso()
        }
        requests_logged.append(item)
        if t:
            trackers_logged.append(item)

    page.on("request", on_request)

    print(f"[{session_name}] Navigating to https://www.freshworks.com ...")
    try:
        await page.goto("https://www.freshworks.com", wait_until="networkidle", timeout=45000)
    except Exception as e:
        print(f"[{session_name}] Networkidle note: {e}, waiting 4s...")
        await page.wait_for_timeout(4000)

    await page.wait_for_timeout(3000)

    # Check for Consent Banners (OneTrust, Cookiebot, Osano, Custom)
    banner_selectors = [
        ("#onetrust-banner-sdk", "OneTrust"),
        ("#CybotCookiebotDialog", "Cookiebot"),
        (".osano-cm-window", "Osano"),
        ("div[class*='cookie']", "Generic Cookie Banner"),
        ("div[id*='cookie']", "Generic Cookie Banner"),
        ("div[class*='consent']", "Generic Consent Banner")
    ]
    detected_banner = None
    for sel, b_type in banner_selectors:
        loc = page.locator(sel)
        if await loc.count() > 0 and await loc.first.is_visible():
            detected_banner = (sel, b_type)
            results["pre_consent"]["banner_detected"] = True
            results["pre_consent"]["banner_type"] = b_type
            results["pre_consent"]["banner_text"] = (await loc.first.inner_text())[:400]
            print(f"[{session_name}] Detected {b_type} banner ({sel})!")
            break

    # Look for Reject All / Accept All / Preferences buttons
    common_buttons = [
        "reject", "refuse", "tout refuser", "decline", "deny",
        "accept", "allow all", "accepter", "agree",
        "settings", "preferences", "customize"
    ]
    btn_elements = await page.locator("button, a").all()
    for btn in btn_elements:
        try:
            txt = (await btn.inner_text()).strip().lower()
            for cb in common_buttons:
                if cb in txt and len(txt) < 40 and await btn.is_visible():
                    results["pre_consent"]["buttons_found"][cb] = {
                        "text": txt,
                        "tag": await btn.evaluate("el => el.tagName")
                    }
        except Exception:
            pass

    cookies = await ctx.cookies()
    results["pre_consent"]["cookie_count"] = len(cookies)
    results["pre_consent"]["cookies"] = cookies
    results["pre_consent"]["requests_count"] = len(requests_logged)
    results["pre_consent"]["tracker_requests"] = trackers_logged

    shot_path = OUTPUT_DIR / f"freshworks_{session_name.lower()}_pre_consent.png"
    await page.screenshot(path=str(shot_path), full_page=False)
    print(f"[{session_name}] Screenshot saved: {shot_path.name}")

    print(f"[{session_name}] Pre-consent summary:")
    print(f"   Cookies dropped: {len(cookies)}")
    print(f"   Total requests: {len(requests_logged)}")
    print(f"   Trackers fired: {len(trackers_logged)}")
    for t in trackers_logged[:8]:
        print(f"     -> {t['tracker']}: {t['url'][:80]}")

    await browser.close()
    return results

async def main():
    print("=" * 65)
    print("STARTING FRESHWORKS DUAL-JURISDICTION AUDIT (EU vs INDIA)")
    print("=" * 65)

    all_data = {}
    async with async_playwright() as p:
        # Run 1: European Union (via Psiphon proxy 127.0.0.1:61809)
        all_data["EU_France"] = await audit_session(
            p, "EU_France", {"server": "http://127.0.0.1:61809"}
        )

        # Run 2: Direct (Bypassing proxy, local India connection)
        # Note: In Playwright, if proxy is omitted, it connects directly without proxy
        all_data["India_Direct"] = await audit_session(
            p, "India_Direct", None
        )

    out_file = OUTPUT_DIR / "freshworks_telemetry.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2)

    print("\n" + "=" * 65)
    print("AUDIT COMPLETE! Results saved to:")
    print(f"  {out_file}")
    print("=" * 65)

if __name__ == "__main__":
    asyncio.run(main())
