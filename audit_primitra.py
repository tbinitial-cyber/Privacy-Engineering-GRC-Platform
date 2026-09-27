import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright

OUTPUT_DIR = Path(r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\primitra_audit")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TRACKER_DOMAINS = [
    "google-analytics.com", "googletagmanager.com", "doubleclick.net",
    "facebook.com", "facebook.net", "linkedin.com", "licdn.com",
    "clarity.ms", "hotjar.com", "segment.io", "segment.com",
    "openai.com", "anthropic.com", "intercom.io", "crisp.chat",
    "hubspot.com", "hs-scripts.com", "leadfeeder.com", "cloudflare.com"
]

def identify_vendor(url):
    for d in TRACKER_DOMAINS:
        if d in url:
            return d
    return None

async def audit_primitra():
    print("=" * 60)
    print("STARTING AUDIT OF PRIMITRA (https://www.primitra.in)")
    print("ROUTE: GENUINE INDIA IP")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            viewport={"width": 1366, "height": 768},
            locale="en-IN",
            timezone_id="Asia/Kolkata"
        )
        page = await context.new_page()

        requests_logged = []
        vendors_logged = []
        response_headers = {}

        async def on_request(req):
            vendor = identify_vendor(req.url)
            item = {
                "url": req.url,
                "method": req.method,
                "resource_type": req.resource_type,
                "vendor": vendor
            }
            requests_logged.append(item)
            if vendor:
                vendors_logged.append(item)

        async def on_response(resp):
            if resp.url in ["https://www.primitra.in/", "https://primitra.in/"]:
                nonlocal response_headers
                response_headers = await resp.all_headers()

        page.on("request", on_request)
        page.on("response", on_response)

        print("[1/5] Navigating to https://www.primitra.in ...")
        resp = await page.goto("https://www.primitra.in", wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(6000)

        title = await page.title()
        print(f"      Page Title: {title}")
        print(f"      Final URL: {page.url}")

        # Check for Consent Banner
        print("[2/5] Inspecting for Consent Banner / CMP...")
        banner_selectors = [
            "#onetrust-banner-sdk",
            "#CybotCookiebotDialog",
            ".cookie-banner",
            "div[id*='cookie']",
            "div[class*='cookie']",
            "div[id*='consent']",
            "div[class*='consent']"
        ]
        detected_banner = None
        for sel in banner_selectors:
            try:
                loc = page.locator(sel)
                if await loc.count() > 0 and await loc.first.is_visible():
                    txt = (await loc.first.text_content()) or ""
                    detected_banner = {
                        "selector": sel,
                        "text": txt[:300].strip()
                    }
                    print(f"      Banner Found: {sel}")
                    break
            except Exception:
                pass

        if not detected_banner:
            print("      NO Consent Banner detected on page load!")

        # Extract all Links (Privacy Policy, AI, Services, etc.)
        print("[3/5] Extracting Navigation & Legal Links...")
        links = await page.locator("a[href]").all()
        link_list = []
        for l in links:
            try:
                href = await l.get_attribute("href")
                text = ((await l.text_content()) or "").strip()
                if href and len(text) > 0:
                    link_list.append({"text": text, "href": href})
            except Exception:
                pass

        # Identify legal / AI specific links
        legal_links = [l for l in link_list if any(k in l["href"].lower() or k in l["text"].lower() for k in ["privacy", "terms", "cookie", "ai", "governance", "compliance", "contact", "about", "career"])]
        print(f"      Total Links Found: {len(link_list)}")
        print(f"      Key Governance / Legal Links:")
        for ll in legal_links:
            print(f"        -> [{ll['text']}] {ll['href']}")

        # Cookies
        print("[4/5] Inspecting Cookies Deposited Pre-Consent...")
        cookies = await context.cookies()
        print(f"      Total Cookies Dropped: {len(cookies)}")
        for c in cookies:
            print(f"        -> Cookie: {c['name']} (Domain: {c['domain']}, Secure: {c['secure']}, HttpOnly: {c['httpOnly']})")

        # Trackers / Vendors
        print(f"[5/5] Third-Party Vendors & Network Requests...")
        print(f"      Total Requests: {len(requests_logged)}")
        print(f"      Third-Party Vendor Calls: {len(vendors_logged)}")
        for v in vendors_logged:
            print(f"        -> [{v['vendor']}] {v['url'][:85]}")

        # Screenshot
        shot_path = OUTPUT_DIR / "primitra_homepage.png"
        await page.screenshot(path=str(shot_path), full_page=True)
        print(f"      Full page screenshot saved: {shot_path.name}")

        # Extract Page Headings
        headings = []
        try:
            head_elements = await page.locator("h1, h2, h3").all()
            for h in head_elements:
                headings.append(((await h.text_content()) or "").strip())
        except Exception:
            pass

        # Save HTML
        html_content = await page.content()
        (OUTPUT_DIR / "primitra_homepage.html").write_text(html_content, encoding="utf-8")

        report = {
            "target": "https://www.primitra.in",
            "audit_timestamp": "2026-09-26T16:38:00Z",
            "page_title": title,
            "final_url": page.url,
            "security_headers": response_headers,
            "consent_banner": detected_banner,
            "cookies_count": len(cookies),
            "cookies": cookies,
            "total_requests": len(requests_logged),
            "vendor_requests_count": len(vendors_logged),
            "vendor_requests": vendors_logged,
            "key_links": legal_links,
            "headings_sample": headings[:15]
        }

        with open(OUTPUT_DIR / "primitra_audit_report.json", "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        print("\nAudit saved to:")
        print(f"  {OUTPUT_DIR / 'primitra_audit_report.json'}")

        # Now let's visit their Privacy Policy if available
        privacy_link = next((l["href"] for l in legal_links if "privacy" in l["href"].lower()), None)
        if privacy_link:
            if not privacy_link.startswith("http"):
                privacy_link = "https://www.primitra.in" + (privacy_link if privacy_link.startswith("/") else "/" + privacy_link)
            print(f"\n[BONUS] Inspecting Privacy Policy at {privacy_link} ...")
            try:
                p_page = await context.new_page()
                await p_page.goto(privacy_link, wait_until="domcontentloaded", timeout=20000)
                await p_page.wait_for_timeout(3000)
                p_html = await p_page.content()
                (OUTPUT_DIR / "primitra_privacy_policy.html").write_text(p_html, encoding="utf-8")
                p_text = ((await p_page.locator("body").text_content()) or "").strip()
                (OUTPUT_DIR / "primitra_privacy_policy.txt").write_text(p_text, encoding="utf-8")
                print("      Privacy Policy content captured!")
                await p_page.close()
            except Exception as pe:
                print(f"      Could not fetch privacy policy: {pe}")

        await browser.close()
        return report

if __name__ == "__main__":
    asyncio.run(audit_primitra())
