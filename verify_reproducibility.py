import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\freshworks_audit\reproducibility_evidence")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TRACKER_DOMAINS = [
    "clarity.ms", "google-analytics.com", "googletagmanager.com", 
    "doubleclick.net", "facebook.com", "facebook.net", "linkedin.com", 
    "licdn.com", "marketo.net", "marketo.com", "bizible.com", 
    "demandbase.com", "quora.com", "bing.com", "bat.bing.com"
]

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def identify_tracker(url):
    for d in TRACKER_DOMAINS:
        if d in url:
            return d
    return None

async def run_single_test(run_id):
    print(f"\n[RUN {run_id}] Starting isolated clean incognito session...")
    har_path = OUTPUT_DIR / f"freshworks_india_run_{run_id}.har"
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            viewport={"width": 1366, "height": 768},
            locale="en-IN",
            timezone_id="Asia/Kolkata",
            record_har_path=str(har_path)
        )
        page = await context.new_page()

        trackers = []
        all_requests = []

        async def on_request(req):
            t = identify_tracker(req.url)
            item = {
                "url": req.url,
                "method": req.method,
                "resource_type": req.resource_type,
                "tracker": t,
                "timestamp": now_iso()
            }
            all_requests.append(item)
            if t:
                trackers_logged = [x["url"] for x in trackers]
                if req.url not in trackers_logged:
                    trackers.append(item)

        page.on("request", on_request)

        # 1. Verify GeoIP seen by browser
        try:
            geo_resp = await page.goto("https://geolocation.onetrust.com/cookieconsentpub/v1/geo/location", timeout=15000)
            geo_text = await geo_resp.text()
        except Exception:
            geo_text = "error"

        # 2. Navigate to freshworks.com
        await page.goto("https://www.freshworks.com", wait_until="domcontentloaded", timeout=35000)
        await page.wait_for_timeout(8000)

        active_groups = await page.evaluate("() => window.OnetrustActiveGroups || null")
        onetrust_geo = await page.evaluate("() => window.OneTrust?.getGeolocationData ? window.OneTrust.getGeolocationData() : null")
        
        banner = page.locator("#onetrust-banner-sdk")
        banner_vis = await banner.is_visible()
        
        reject_btn = page.locator("#onetrust-reject-all-handler")
        reject_vis = await reject_btn.is_visible()
        
        accept_btn = page.locator("#onetrust-accept-btn-handler")
        accept_vis = await accept_btn.is_visible()

        cookies = await context.cookies()

        shot_path = OUTPUT_DIR / f"freshworks_india_run_{run_id}.png"
        await page.screenshot(path=str(shot_path), full_page=False)

        run_summary = {
            "run_id": run_id,
            "timestamp": now_iso(),
            "direct_geoip_endpoint": geo_text.strip(),
            "onetrust_detected_geoip": onetrust_geo,
            "onetrust_active_groups": active_groups,
            "banner_visible": banner_vis,
            "reject_all_button_visible": reject_vis,
            "accept_all_button_visible": accept_vis,
            "cookies_dropped_count": len(cookies),
            "total_network_requests": len(all_requests),
            "distinct_tracker_endpoints_count": len(trackers),
            "trackers_fired": trackers,
            "cookies": [{
                "name": c["name"],
                "domain": c["domain"],
                "secure": c["secure"],
                "httpOnly": c["httpOnly"],
                "sameSite": c["sameSite"]
            } for c in cookies]
        }

        with open(OUTPUT_DIR / f"freshworks_india_run_{run_id}.json", "w", encoding="utf-8") as f:
            json.dump(run_summary, f, indent=2)

        print(f"[RUN {run_id}] Summary:")
        print(f"   GeoIP: {onetrust_geo}")
        print(f"   Active Groups: {active_groups}")
        print(f"   Reject All button visible: {reject_vis}")
        print(f"   Cookies dropped: {len(cookies)}")
        print(f"   Trackers fired: {len(trackers)}")
        print(f"   HAR archived: {har_path.name}")

        await browser.close()
        return run_summary

async def main():
    print("=" * 60)
    print("RUNNING MULTI-PASS REPRODUCIBILITY VERIFICATION (INDIA)")
    print("=" * 60)
    res1 = await run_single_test(1)
    await asyncio.sleep(3)
    res2 = await run_single_test(2)
    
    consistent = (
        res1["onetrust_active_groups"] == res2["onetrust_active_groups"] and
        res1["reject_all_button_visible"] == res2["reject_all_button_visible"] and
        abs(res1["cookies_dropped_count"] - res2["cookies_dropped_count"]) <= 3 and
        abs(res1["distinct_tracker_endpoints_count"] - res2["distinct_tracker_endpoints_count"]) <= 2
    )

    print("\n" + "=" * 60)
    print(f"MULTI-PASS REPRODUCIBILITY VERIFIED: {consistent}")
    print(f"Run 1 Active Groups: {res1['onetrust_active_groups']} | Run 2: {res2['onetrust_active_groups']}")
    print(f"Run 1 Reject Button: {res1['reject_all_button_visible']} | Run 2: {res2['reject_all_button_visible']}")
    print(f"Run 1 Cookies: {res1['cookies_dropped_count']} | Run 2 Cookies: {res2['cookies_dropped_count']}")
    print(f"Run 1 Trackers: {res1['distinct_tracker_endpoints_count']} | Run 2 Trackers: {res2['distinct_tracker_endpoints_count']}")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
