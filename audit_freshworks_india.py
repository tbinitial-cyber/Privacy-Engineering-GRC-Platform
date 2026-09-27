import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\freshworks_audit")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TRACKER_DOMAINS = [
    "clarity.ms",
    "google-analytics.com",
    "googletagmanager.com",
    "doubleclick.net",
    "facebook.com",
    "facebook.net",
    "linkedin.com",
    "licdn.com",
    "marketo.net",
    "marketo.com",
    "bizible.com",
    "demandbase.com",
    "quora.com",
    "bing.com",
    "bat.bing.com",
    "hotjar.com",
    "segment.io",
    "segment.com"
]

def identify_tracker(url):
    for d in TRACKER_DOMAINS:
        if d in url:
            return d
    return None

async def run_india_audit():
    print("=" * 60)
    print("STARTING FRESHWORKS GENUINE INDIA (DPDPA) AUDIT")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            viewport={"width": 1366, "height": 768},
            locale="en-IN",
            timezone_id="Asia/Kolkata"
        )
        page = await ctx.new_page()

        trackers_fired = []
        all_requests = []

        async def on_request(req):
            t = identify_tracker(req.url)
            item = {
                "url": req.url,
                "method": req.method,
                "resource_type": req.resource_type,
                "tracker": t
            }
            all_requests.append(item)
            if t:
                trackers_fired.append(item)

        page.on("request", on_request)

        print("[1/5] Navigating to https://www.freshworks.com from India IP...")
        await page.goto("https://www.freshworks.com", wait_until="domcontentloaded", timeout=40000)
        print("[2/5] Page loaded. Waiting 8s for telemetry settling...")
        await page.wait_for_timeout(8000)

        # Inspect OneTrust Geolocation and Groups
        print("[3/5] Extracting OneTrust state and GeoIP...")
        geoip = await page.evaluate("() => window.OneTrust?.getGeolocationData ? window.OneTrust.getGeolocationData() : null")
        active_groups = await page.evaluate("() => window.OnetrustActiveGroups || null")
        print(f"      GeoIP detected by page: {geoip}")
        print(f"      Active Groups: {active_groups}")

        # Check Banner and Buttons
        print("[4/5] Checking Consent Banner in India...")
        banner = page.locator("#onetrust-banner-sdk")
        banner_vis = await banner.is_visible()
        banner_text = (await banner.inner_text()) if banner_vis else None

        reject_btn = page.locator("#onetrust-reject-all-handler")
        reject_vis = await reject_btn.is_visible()
        reject_text = (await reject_btn.inner_text()).strip() if reject_vis else None

        accept_btn = page.locator("#onetrust-accept-btn-handler")
        accept_vis = await accept_btn.is_visible()
        accept_text = (await accept_btn.inner_text()).strip() if accept_vis else None

        settings_btn = page.locator("#onetrust-pc-btn-handler")
        settings_vis = await settings_btn.is_visible()

        print(f"      Banner Visible: {banner_vis}")
        print(f"      Accept All Visible: {accept_vis} ('{accept_text}')")
        print(f"      Reject All Visible: {reject_vis} ('{reject_text}')")
        print(f"      Cookie Settings Visible: {settings_vis}")

        # Cookies
        print("[5/5] Analyzing Cookies and Trackers Pre-Consent...")
        cookies = await ctx.cookies()
        print(f"      Total Cookies Dropped: {len(cookies)}")
        print(f"      Total Requests: {len(all_requests)}")
        print(f"      Trackers Fired: {len(trackers_fired)}")

        for t in trackers_fired:
            print(f"        -> [{t['tracker']}] {t['url'][:80]}")

        shot_path = OUTPUT_DIR / "freshworks_india_live_pre_consent.png"
        await page.screenshot(path=str(shot_path), full_page=False)

        report = {
            "jurisdiction": "India",
            "target": "https://www.freshworks.com",
            "geoip_detected": geoip,
            "onetrust_active_groups": active_groups,
            "banner": {
                "visible": banner_vis,
                "text": banner_text[:400] if banner_text else None,
                "accept_all_visible": accept_vis,
                "accept_all_text": accept_text,
                "reject_all_visible": reject_vis,
                "reject_all_text": reject_text,
                "settings_visible": settings_vis
            },
            "cookie_count": len(cookies),
            "cookies": [{
                "name": c["name"],
                "value_length": len(c["value"]),
                "domain": c["domain"],
                "path": c["path"],
                "secure": c["secure"],
                "httpOnly": c["httpOnly"],
                "sameSite": c["sameSite"]
            } for c in cookies],
            "trackers_count": len(trackers_fired),
            "trackers_fired": trackers_fired,
            "total_requests": len(all_requests)
        }

        report_file = OUTPUT_DIR / "freshworks_india_telemetry.json"
        with open(report_file, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print("\n" + "=" * 60)
        print("INDIA AUDIT FINISHED!")
        print(f"Report saved to: {report_file}")
        print("=" * 60)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_india_audit())
