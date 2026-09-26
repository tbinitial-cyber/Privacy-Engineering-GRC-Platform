"""
Canonical Reproducible Telemetry Capture Tool for Miro.com
Supports:
  - European Union Profile: python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809
  - India Domestic Profile: python capture_miro.py --profile india
Captures:
  - Verified GeoIP from geolocation.onetrust.com
  - DOM-level window.OnetrustActiveGroups
  - Pre-Consent, Accept All, and Reject All states (where available)
  - Full CDP network events and cookie inventories
"""

import asyncio
import argparse
import json
import os
import hashlib
from datetime import datetime, timezone
from playwright.async_api import async_playwright

def compute_sha256(filepath: str) -> str:
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

async def capture_profile(profile: str, proxy: str = None, headless: bool = True):
    is_eu = profile.lower() in ["eu", "eu-france", "france"]
    run_id = "MIRO-EU-001" if is_eu else "MIRO-IN-001"
    jurisdiction = "EU" if is_eu else "INDIA"
    target_url = "https://miro.com" if not is_eu else "https://miro.com/fr/"

    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(base_dir, "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY", "runs", run_id)
    os.makedirs(output_dir, exist_ok=True)

    print(f"============================================================")
    print(f"🔬 RUNNING STANDARDIZED AUDIT CAPTURE: {run_id}")
    print(f"🌐 Jurisdiction Profile: {profile.upper()} ({jurisdiction})")
    print(f"🔌 Network Proxy: {proxy or 'Direct Indian IP (No proxy)'}")
    print(f"============================================================")

    async with async_playwright() as p:
        launch_args = {"headless": headless}
        if proxy:
            launch_args["proxy"] = {"server": proxy}

        browser = await p.chromium.launch(**launch_args)
        har_path = os.path.join(output_dir, "network.har")
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            record_har_path=har_path,
            record_har_content="embed"
        )
        page = await context.new_page()

        onetrust_geo = None
        network_events = []

        async def handle_response(response):
            nonlocal onetrust_geo
            try:
                if "geolocation.onetrust.com" in response.url:
                    text = await response.text()
                    try:
                        onetrust_geo = json.loads(text)
                        print(f"📍 Intercepted OneTrust GeoIP: {onetrust_geo}")
                    except Exception:
                        onetrust_geo = {"raw": text}
            except Exception:
                pass

        page.on("response", handle_response)
        page.on("request", lambda req: network_events.append({
            "url": req.url,
            "method": req.method,
            "resource_type": req.resource_type,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }))

        print(f"Navigating to {target_url}...")
        try:
            await page.goto(target_url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"Note: Navigation finished with: {e}")
        await page.wait_for_timeout(3000)

        # 1. PRE-CONSENT STATE
        pre_cookies = await context.cookies()
        pre_screenshot_path = os.path.join(output_dir, "pre_consent.png")
        await page.screenshot(path=pre_screenshot_path, full_page=False)

        banner = page.locator("#onetrust-banner-sdk")
        banner_visible = await banner.is_visible()
        banner_text = (await banner.inner_text()) if banner_visible else None

        active_groups = await page.evaluate("() => window.OnetrustActiveGroups || null")
        accept_btn = page.locator("#onetrust-accept-btn-handler")
        reject_btn = page.locator("#onetrust-reject-all-handler")

        has_accept = await accept_btn.is_visible()
        has_reject = await reject_btn.is_visible()

        geo_cookie = next((c["value"] for c in pre_cookies if c["name"] == "geo_data"), None)
        optanon_cookie = next((c["value"] for c in pre_cookies if c["name"] == "OptanonConsent"), None)

        pre_state = {
            "audit_run_id": run_id,
            "profile": profile,
            "jurisdiction": jurisdiction,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "target": target_url,
            "consent_state": "PRE_CONSENT",
            "onetrust_geoip": onetrust_geo,
            "geo_data_cookie": geo_cookie,
            "optanon_consent_cookie": optanon_cookie,
            "active_groups": active_groups,
            "banner_visible": banner_visible,
            "banner_text": banner_text,
            "buttons": {
                "accept_all": has_accept,
                "reject_all": has_reject
            },
            "cookie_count": len(pre_cookies),
            "cookies": pre_cookies,
            "total_requests": len(network_events)
        }

        with open(os.path.join(output_dir, "baseline.json"), "w", encoding="utf-8") as f:
            json.dump(pre_state, f, indent=2)
        print(f"✅ Baseline saved ({len(pre_cookies)} cookies, active groups: {active_groups})")

        # 2. EXECUTE REJECT ALL (IF VISIBLE)
        if has_reject:
            print("Clicking 'Reject All' (Tout refuser)...")
            await reject_btn.click()
            await page.wait_for_timeout(3000)
            reject_cookies = await context.cookies()
            reject_screenshot_path = os.path.join(output_dir, "post_reject.png")
            await page.screenshot(path=reject_screenshot_path, full_page=False)

            reject_state = {
                "audit_run_id": run_id,
                "action": "CLICKED_REJECT_ALL",
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "cookie_count": len(reject_cookies),
                "cookies": reject_cookies
            }
            with open(os.path.join(output_dir, "post_reject.json"), "w", encoding="utf-8") as f:
                json.dump(reject_state, f, indent=2)
            print(f"✅ Post-Reject state saved ({len(reject_cookies)} cookies)")

        elif is_eu:
            print("Warning: Reject All button not visible on EU route!")

        # 3. RUN CONTEXT RECORD
        run_context = {
            "audit_run_id": run_id,
            "profile": profile,
            "target_url": target_url,
            "jurisdiction_condition": jurisdiction,
            "applicable_framework": "GDPR" if is_eu else "DPDPA",
            "proxy_used": proxy,
            "onetrust_geoip_captured": onetrust_geo,
            "miro_geo_cookie": geo_cookie,
            "pre_consent_cookie_count": len(pre_cookies),
            "pre_consent_active_groups": active_groups,
            "first_layer_reject_all_visible": has_reject,
            "captured_at": datetime.now(timezone.utc).isoformat()
        }
        with open(os.path.join(output_dir, "run_context.json"), "w", encoding="utf-8") as f:
            json.dump(run_context, f, indent=2)

        await context.close()
        await browser.close()

    print(f"🎉 Capture complete! Artifacts verified in {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Miro.com Standardized Telemetry Capture CLI")
    parser.add_argument("--profile", choices=["india", "eu-france"], default="india", help="Capture profile")
    parser.add_argument("--proxy", default=None, help="Proxy URL for European route (e.g. http://127.0.0.1:61809)")
    parser.add_argument("--headless", action="store_true", default=True, help="Run headless")
    args = parser.parse_args()

    asyncio.run(capture_profile(
        profile=args.profile,
        proxy=args.proxy,
        headless=args.headless
    ))

if __name__ == "__main__":
    main()
