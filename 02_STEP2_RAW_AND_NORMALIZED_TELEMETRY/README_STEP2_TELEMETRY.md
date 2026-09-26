# 🌐 FOLDER 02: Step 2 - Raw & Normalized Telemetry Evidence

### What is in this folder?
- `normalized_evidence.json`: 301 structured records (65 cookies + 236 HTTP network events) validated against Step 1's schema. Every record has a unique SHA-256 fingerprint (e.g. `EVD-WEB-001-CDEB879188`).
- `pre_consent.png`: Full screenshot of Miro showing the cookie banner BEFORE clicking anything.
- `post_consent.png`: Full screenshot of Miro AFTER clicking "Accept All".
- `baseline.json`: The 55 unique cookies that were dropped on the computer BEFORE consent (Pre-Consent Baseline).
- `post_consent.json`: The 65 total cookies present AFTER clicking "Accept All" (including 10 brand-new cookies released post-consent).
- `host_inventory.json`: List of all 74 external companies/servers Miro connected to.
- `network.har`: The complete 26.1 MB HTTP Archive (HAR) file containing browser-level HTTP request/response network telemetry.

### Plain English Explanation:
- **What did we do?** We opened a real web browser (Playwright Chromium) and visited `https://miro.com`.
- **Pre-Consent:** We recorded what cookies and network calls loaded before touching the banner.
- **Post-Consent:** You physically clicked "Accept All", and we recorded what fired immediately afterward.
- **Normalization:** We took thousands of raw web events, removed duplicate noise, and gave each event a permanent SHA-256 ID so no one can tamper with it.
