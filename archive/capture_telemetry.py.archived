"""
Universal Privacy Engineering Telemetry Capture CLI
Standardized CDP / Playwright instrument for multi-jurisdiction comparative consent gate audits.
Supports: Direct domestic capture (India) and Proxied/VPN capture (European Union).
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

async def run_capture(target_url: str, jurisdiction: str, run_id: str, proxy: str = None, action: str = "accept", headless: bool = True, output_dir: str = None):
    print(f"================================================================")
    print(f"🔒 PRIVACY TELEMETRY CAPTURE ENGINE: {run_id}")
    print(f"🌐 Target: {target_url} | Jurisdiction: {jurisdiction}")
    print(f"🔌 Proxy: {proxy or 'Direct connection (no proxy)'}")
    print(f"================================================================")

    if not output_dir:
        output_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "02_STEP2_RAW_AND_NORMALIZED_TELEMETRY",
            "runs",
            run_id
        )
    os.makedirs(output_dir, exist_ok=True)

    network_events = []
    
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

        # Intercept and log network requests
        onetrust_geo_response = None
        
        async def on_response(response):
            nonlocal onetrust_geo_response
            try:
                if "geolocation.onetrust.com" in response.url:
                    text = await response.text()
                    try:
                        onetrust_geo_response = json.loads(text)
                        print(f"📍 OneTrust GeoIP captured: {onetrust_geo_response}")
                    except Exception:
                        onetrust_geo_response = text
            except Exception:
                pass

        page.on("response", on_response)
        page.on("request", lambda req: network_events.append({
            "url": req.url,
            "method": req.method,
            "resource_type": req.resource_type,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }))

        print(f"🚀 Navigating to {target_url}...")
        try:
            await page.goto(target_url, wait_until="networkidle", timeout=60000)
        except Exception as e:
            print(f"⚠️ Page load warning: {e}, waiting 5s for stability...")
        await page.wait_for_timeout(4000)

        # 1. Capture Pre-Consent State
        pre_cookies = await context.cookies()
        pre_img_path = os.path.join(output_dir, "pre_consent.png")
        await page.screenshot(path=pre_img_path, full_page=False)
        print(f"📸 Captured pre-consent screenshot: {pre_img_path}")

        # Check OneTrust DOM & Groups
        banner_locator = page.locator("#onetrust-banner-sdk")
        banner_visible = await banner_locator.is_visible()
        banner_text = (await banner_locator.inner_text()) if banner_visible else None

        active_groups = await page.evaluate("() => window.OnetrustActiveGroups || null")
        
        # Check buttons
        accept_btn = page.locator("#onetrust-accept-btn-handler")
        reject_btn = page.locator("#onetrust-reject-all-handler")
        settings_btn = page.locator("#onetrust-pc-btn-handler")

        has_accept = await accept_btn.is_visible()
        has_reject = await reject_btn.is_visible()
        has_settings = await settings_btn.is_visible()

        accept_text = (await accept_btn.inner_text()) if has_accept else None
        reject_text = (await reject_btn.inner_text()) if has_reject else None

        # Extract Cookies of interest
        geo_cookie = next((c["value"] for c in pre_cookies if c["name"] == "geo_data"), None)
        optanon_cookie = next((c["value"] for c in pre_cookies if c["name"] == "OptanonConsent"), None)

        baseline_data = {
            "audit_run_id": run_id,
            "jurisdiction": jurisdiction,
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "target": target_url,
            "consent_state": "PRE_CONSENT",
            "banner_detected": banner_visible,
            "banner_text": banner_text,
            "buttons": {
                "accept_all": {"visible": has_accept, "text": accept_text},
                "reject_all": {"visible": has_reject, "text": reject_text},
                "cookie_settings": {"visible": has_settings}
            },
            "onetrust_active_groups": active_groups,
            "onetrust_geoip_response": onetrust_geo_response,
            "geo_data_cookie": geo_cookie,
            "optanon_consent_cookie": optanon_cookie,
            "cookie_count": len(pre_cookies),
            "cookies": pre_cookies,
            "request_count": len(network_events)
        }

        with open(os.path.join(output_dir, "baseline.json"), "w", encoding="utf-8") as f:
            json.dump(baseline_data, f, indent=2)

        # 2. Execute Action if requested
        post_cookies = []
        post_action_name = "NONE"

        if action == "reject" and has_reject:
            post_action_name = "CLICKED_REJECT_ALL"
            print(f"🚫 Clicking 'Reject All' button ({reject_text})...")
            await reject_btn.click()
            await page.wait_for_timeout(4000)
            post_cookies = await context.cookies()
            post_img_path = os.path.join(output_dir, "post_reject.png")
            await page.screenshot(path=post_img_path, full_page=False)

        elif action == "accept" and has_accept:
            post_action_name = "CLICKED_ACCEPT_ALL"
            print(f"✅ Clicking 'Accept All' button ({accept_text})...")
            await accept_btn.click()
            await page.wait_for_timeout(4000)
            post_cookies = await context.cookies()
            post_img_path = os.path.join(output_dir, "post_consent.png")
            await page.screenshot(path=post_img_path, full_page=False)

        post_data = {
            "audit_run_id": run_id,
            "jurisdiction": jurisdiction,
            "action_executed": post_action_name,
            "observed_at": datetime.now(timezone.utc).isoformat(),
            "cookie_count": len(post_cookies),
            "cookies": post_cookies
        }

        with open(os.path.join(output_dir, "post_action.json"), "w", encoding="utf-8") as f:
            json.dump(post_data, f, indent=2)

        # 3. Write Run Context
        run_context = {
            "audit_run_id": run_id,
            "target_url": target_url,
            "jurisdiction_condition": jurisdiction,
            "applicable_framework": "GDPR" if jurisdiction == "EU" else "DPDPA",
            "proxy_used": proxy,
            "onetrust_geoip_captured": onetrust_geo_response,
            "miro_geo_cookie": geo_cookie,
            "pre_consent_cookie_count": len(pre_cookies),
            "pre_consent_active_groups": active_groups,
            "first_layer_reject_all_visible": has_reject,
            "post_action_executed": post_action_name,
            "post_action_cookie_count": len(post_cookies),
            "captured_at": datetime.now(timezone.utc).isoformat()
        }

        with open(os.path.join(output_dir, "run_context.json"), "w", encoding="utf-8") as f:
            json.dump(run_context, f, indent=2)

        await context.close()
        await browser.close()

    print(f"🎉 Capture completed successfully for {run_id}!")
    print(f"📂 Output artifacts saved in: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="Empirical Privacy Telemetry Capture CLI")
    parser.add_argument("--target", default="https://miro.com", help="Target URL to audit")
    parser.add_argument("--jurisdiction", choices=["INDIA", "EU", "US"], default="INDIA", help="Jurisdiction condition")
    parser.add_argument("--run-id", required=True, help="Audit run identifier (e.g. MIRO-IN-001, MIRO-EU-001)")
    parser.add_argument("--proxy", default=None, help="Proxy URL (e.g. http://127.0.0.1:61809)")
    parser.add_argument("--action", choices=["accept", "reject", "none"], default="accept", help="Consent banner action")
    parser.add_argument("--headless", action="store_true", default=True, help="Run browser in headless mode")
    parser.add_argument("--output-dir", default=None, help="Custom output directory")
    args = parser.parse_args()

    asyncio.run(run_capture(
        target_url=args.target,
        jurisdiction=args.jurisdiction,
        run_id=args.run_id,
        proxy=args.proxy,
        action=args.action,
        headless=args.headless,
        output_dir=args.output_dir
    ))

if __name__ == "__main__":
    main()
