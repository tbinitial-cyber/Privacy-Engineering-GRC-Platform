import asyncio
from playwright.async_api import async_playwright

async def main():
    print("Launching Chromium to capture clear Pre vs Post consent screenshots...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await context.new_page()
        
        print("Navigating to https://miro.com...")
        await page.goto("https://miro.com", wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(3000)
        
        # Check for OneTrust banner
        banner = page.locator("#onetrust-banner-sdk")
        banner_visible = await banner.is_visible()
        print("Banner visible pre-consent:", banner_visible)
        
        # Take Pre-Consent screenshot (viewport view so banner is clearly visible at bottom)
        pre_path = r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\pre_consent.png"
        await page.screenshot(path=pre_path, full_page=False)
        print("Saved clear pre_consent.png (with banner visible)")
        
        # Click Accept All button
        accept_btn = page.locator("#onetrust-accept-btn-handler")
        if await accept_btn.is_visible():
            print("Clicking 'Accept All' button (#onetrust-accept-btn-handler)...")
            await accept_btn.click()
            await page.wait_for_timeout(3000)
            
            # Wait for banner to hide
            try:
                await banner.wait_for(state="hidden", timeout=5000)
                print("Banner is now hidden!")
            except Exception as e:
                print("Banner hide wait timed out, continuing...")
                
        # Take Post-Consent screenshot (banner now completely dismissed!)
        post_path = r"C:\Users\acer\Privacy_Engineering_Master_Portfolio\02_STEP2_RAW_AND_NORMALIZED_TELEMETRY\post_consent.png"
        await page.screenshot(path=post_path, full_page=False)
        print("Saved clear post_consent.png (banner completely dismissed!)")
        
        await browser.close()
        print("Screenshots updated successfully!")

if __name__ == "__main__":
    asyncio.run(main())
