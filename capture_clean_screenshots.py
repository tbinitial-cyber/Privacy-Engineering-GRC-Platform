"""
Standardized Screen & Telemetry Capture CLI Wrapper
Supports both EU and India routes with identical flags as capture_miro.py:
  python capture_clean_screenshots.py --profile india
  python capture_clean_screenshots.py --profile eu-france --proxy http://127.0.0.1:61809
"""

import sys
import os
import argparse
import asyncio

# Ensure repo root is in python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from capture_miro import capture_profile

def main():
    parser = argparse.ArgumentParser(description="Miro.com Standardized Multi-Jurisdiction Capture CLI")
    parser.add_argument("--profile", choices=["india", "eu-france", "france", "eu"], default="india", help="Jurisdiction profile to capture")
    parser.add_argument("--proxy", default=None, help="Proxy URL for European route (e.g. http://127.0.0.1:61809)")
    parser.add_argument("--headless", action="store_true", default=True, help="Run headless browser session")
    args = parser.parse_args()

    print(f"[*] Starting standardized capture wrapper: profile={args.profile}, proxy={args.proxy}")
    asyncio.run(capture_profile(
        profile=args.profile,
        proxy=args.proxy,
        headless=args.headless
    ))

if __name__ == "__main__":
    main()
