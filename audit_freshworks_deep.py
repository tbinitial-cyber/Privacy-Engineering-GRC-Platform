import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\freshworks_audit")

async def test_freshworks_deep(proxy_url, label):
    print(f"=== Testing Freshworks [{label}] ===")
    async with async_playwright() as p:
        launch_kwargs = {
            "headless": True,
            "args": ["--disable-blink-features=AutomationControlled"]
        }
        if proxy_url:
            launch_kwargs["proxy"] = {"server": proxy_url}

        browser = await p.chromium.launch(**launch_kwargs)
        ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            viewport={"width": 1366, "height": 768},
            locale="fr-FR" if proxy_url else "en-IN"
        )
        page = await ctx.new_page()

        trackers = []
        page.on("request", lambda r: trackers.append({
            "url": r.url,
            "method": r.method,
            "resource_type": r.resource_type
        }) if any(k in r.url for k in [
            "clarity.ms", "google-analytics.com", "googletagmanager.com", 
            "doubleclick.net", "facebook.net", "linkedin.com", "marketo.net", 
            "bizible.com", "demandbase.com", "hotjar.com", "quora.com", "bing.com"
        ]) else None)

        await page.goto("https://www.freshworks.com", wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(6000)

        banner = page.locator("#onetrust-banner-sdk")
        banner_vis = await banner.is_visible()
        banner_text = (await banner.inner_text()) if banner_vis else "Not visible"

        reject_btn = page.locator("#onetrust-reject-all-handler")
        reject_vis = await reject_btn.is_visible()

        accept_btn = page.locator("#onetrust-accept-btn-handler")
        accept_vis = await accept_btn.is_visible()

        cookies = await ctx.cookies()
        active_groups = await page.evaluate("() => window.OnetrustActiveGroups || 'None'")
        geoip = await page.evaluate("() => window.OneTrust?.getGeolocationData ? window.OneTrust.getGeolocationData() : null")

        print(f"[{label}] Banner visible:", banner_vis)
        print(f"[{label}] Reject button visible:", reject_vis)
        print(f"[{label}] Accept button visible:", accept_vis)
        print(f"[{label}] Active Groups:", active_groups)
        print(f"[{label}] Pre-consent cookies:", len(cookies))
        print(f"[{label}] Pre-consent third-party tracker requests:", len(trackers))
        for t in trackers[:6]:
            print(f"   -> {t['url'][:85]}")

        await page.screenshot(path=str(OUTPUT_DIR / f"freshworks_{label.lower()}_banner.png"))

        report = {
            "label": label,
            "banner_visible": banner_vis,
            "banner_text": banner_text[:300],
            "reject_button_visible": reject_vis,
            "accept_button_visible": accept_vis,
            "active_groups": active_groups,
            "geoip": geoip,
            "cookie_count": len(cookies),
            "cookies": [{
                "name": c["name"],
                "domain": c["domain"],
                "secure": c["secure"],
                "httpOnly": c["httpOnly"],
                "sameSite": c["sameSite"]
            } for c in cookies],
            "tracker_count": len(trackers),
            "trackers": trackers
        }

        with open(OUTPUT_DIR / f"freshworks_{label.lower()}_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        await browser.close()

async def main():
    # 1. Test Europe (France)
    await test_freshworks_deep("http://127.0.0.1:61809", "EU_France")
    # 2. Test India (Direct)
    await test_freshworks_deep(None, "India_Direct")

if __name__ == "__main__":
    asyncio.run(main())
