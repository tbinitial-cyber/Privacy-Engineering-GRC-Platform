# 🔍 FOLDER 04: Step 4 - Transparency Reconciliation & Cookie Inventory

### What is in this folder?
- `TRANSPARENCY_RECONCILIATION_REPORT.md` / `.json`: The reconciliation report comparing technical reality vs. Miro's legal documents.
- `COOKIE_VENDOR_INVENTORY.md` / `.json`: The complete register mapping all 65 captured cookies to vendors, categories, and consent states.

### Plain English Explanation:
- **What is Reconciliation?** We took Miro's official Privacy Policy and July 2026 Subprocessor List and compared them against what the browser actually captured.
- **The "Audit Gotchas" Found:**
  - **Disclosed:** Intercom (Chatbot) and OpenAI are properly disclosed.
  - **Partially Disclosed:** Google Looker is disclosed, but Google DoubleClick ad tracking is omitted.
  - **Completely Undisclosed:** Tapad (cross-device sync), Reddit Pixel, Spotify Pixel, Hotjar (screen recording), and Microsoft Clarity were completely missing from the official subprocessor list!
