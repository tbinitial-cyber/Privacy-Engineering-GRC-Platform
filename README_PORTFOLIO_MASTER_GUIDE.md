# 🏆 PRIVACY ENGINEERING & GRC TECHNICAL AUDIT PORTFOLIO
### *End-to-End Audit-Grade Compliance Pipeline: Frontend Web Telemetry to Statutory RoPA, DPIA & Vendor Contracts*
**Audited Subject:** Miro Web Platform (`https://miro.com`)  
**Audit Reference:** `miro_live_audit_run_001`  
**Master Folder Location:** `C:\Users\acer\Privacy_Engineering_Master_Portfolio`  
**Author:** Dual-Domain Privacy Engineering & Category 2 GRC Professional  

---

## 🚀 LAUNCH THE INTERACTIVE WEB DASHBOARD (BASE 1 PROJECT)

You can launch the complete, interactive web application with a single command or click:
1. **Option A (One-Click):** Double-click [`run_app.bat`](file:///C:/Users/acer/Privacy_Engineering_Master_Portfolio/run_app.bat) in this folder.
2. **Option B (Terminal):** Open PowerShell or Terminal and run:
   ```bash
   cd "C:\Users\acer\Privacy_Engineering_Master_Portfolio"
   python -m streamlit run app.py
   ```
3. Open your browser at: **`http://localhost:8501`**

This will open an interactive corporate compliance portal with live screenshot viewers, cookie filter bars, downloadable Excel RoPAs, DPIA risk matrices, and vendor contract redlining tools.

---

## 🗺️ How This Master Portfolio Is Organized

This portfolio is divided into **10 dedicated folders** so nothing is mixed up. Each folder represents one logical step in an enterprise compliance workflow:

```
C:\Users\acer\Privacy_Engineering_Master_Portfolio\
├── 📁 00_STUDY_GUIDES_GDPR_DPDPA
│   ├── 📜 DPDPA_2023_COMPLETE_SECTION_CODEBOOK.md (Complete 44-section breakdown of India DPDPA)
│   ├── 📜 CCPA_CPRA_OPERATIONAL_MASTER_GUIDE.md (California / US operational master guide)
│   ├── 📜 GDPR_DPDPA_CCPA_3WAY_COMPARATIVE_MASTER.md (The 15-dimension 3-way Rosetta Stone)
│   ├── 📜 PRIVACY_MASTER_TEXTBOOK_GDPR_DPDPA.md (Foundational GDPR vs DPDPA textbook)
│   └── 📘 README_STEP00_STUDY_GUIDE.md
│
├── 📁 01_STEP1_CANONICAL_SCHEMA
│   ├── 📐 evidence.schema.json (The master JSON Schema Draft 2020-12 contract)
│   └── 📘 README_STEP1_SCHEMA.md
│
├── 📁 02_STEP2_RAW_AND_NORMALIZED_TELEMETRY
│   ├── 🌐 normalized_evidence.json (301 records with deterministic SHA-256 IDs)
│   ├── 🍪 baseline.json (55 unique pre-consent cookies)
│   ├── 🍪 post_consent.json (65 total post-consent cookies)
│   ├── 🖥️ host_inventory.json (74 external hosts discovered)
│   ├── 📸 pre_consent.png (Full-page screenshot showing OneTrust banner)
│   ├── 📸 post_consent.png (Full-page screenshot after clicking Accept All)
│   ├── 📦 network.har (26.1 MB binary network recording file)
│   └── 📘 README_STEP2_TELEMETRY.md
│
├── 📁 03_STEP3_CANDIDATE_ACTIVITIES
│   ├── 🧩 candidate_processing_activities.json (5 grouped business activities)
│   └── 📘 README_STEP3_CANDIDATE_ACTIVITIES.md
│
├── 📁 04_STEP4_TRANSPARENCY_AND_COOKIE_REGISTER
│   ├── 🔍 TRANSPARENCY_RECONCILIATION_REPORT.md (Technical reality vs Privacy Policy)
│   ├── 📊 transparency_reconciliation_report.json
│   ├── 🍪 COOKIE_VENDOR_INVENTORY.md (65 cookies grouped by vendor and category)
│   ├── 📋 cookie_vendor_inventory.json
│   └── 📘 README_STEP4_TRANSPARENCY.md
│
├── 📁 05_STEP5_ARTICLE_30_ROPA_REGISTER
│   ├── 📊 ROPA_ARTICLE_30_REGISTER.xlsx (Enterprise 4-sheet corporate Excel workbook)
│   ├── 🏛️ ROPA_ARTICLE_30_REGISTER.md (Complete statutory register under GDPR Art 30 / DPDPA Sec 8)
│   └── 📘 README_STEP5_ROPA.md
│
├── 📁 06_STEP6_DPIA_SCREENING_NOTE
│   ├── 🛡️ DPIA_SCREENING_NOTE.md (EDPB WP 248 9-criteria risk assessment for Clarity & Tapad)
│   └── 📘 README_STEP6_DPIA.md
│
├── 📁 07_STEP7_VENDOR_DPA_REDLINE_PLAYBOOK
│   ├── 📑 VENDOR_DPA_REDLINE_PLAYBOOK.md (7 master clause redlines under GDPR Art 28 & SCCs)
│   └── 📘 README_STEP7_DPA_PLAYBOOK.md
│
├── 📁 08_REAL_WORLD_DPA_BENCHMARK_SAMPLES
│   ├── 📑 01_AWS to 10_Zoho Analyses (10-point battleground dissection of 10 global giants)
│   ├── 📊 MASTER_10_DPA_COMPARATIVE_SCORECARD.xlsx (Color-coded Excel scorecard & SLA matrix)
│   └── 📘 README_DPA_BENCHMARK_GUIDE.md
│
├── 📁 09_PRIVACY_POLICIES_AND_TRANSPARENCY_GOVERNANCE
│   ├── 🌐 FULL_GLOBAL_PRIVACY_POLICY_MASTER_SPECIMEN.md (GDPR, DPDPA & CCPA compliant notice)
│   ├── 📋 PRIVACY_POLICY_AUDIT_CHECKLIST.md (25-point technical truth alignment checklist)
│   ├── 🛠️ HOW_TO_DRAFT_A_PRIVACY_POLICY_FROM_ROPA.md (RoPA-to-Policy translation matrix)
│   └── 📘 README_PRIVACY_POLICY_GUIDE.md
│
└── 📘 README_PORTFOLIO_MASTER_GUIDE.md (This Master Guide)
```

---

## 🧭 The Plain-English Story of What We Built

If you ever feel lost or need to explain this project in an interview, here is the simple 7-step story:

1. **Step 1 (The Rulebook):** We wrote a strict JSON Schema (`evidence.schema.json`) that sets the ground rules. No telemetry data is accepted unless it satisfies this exact mathematical format.
2. **Step 2 (The Live Crime Scene Capture):** We launched a real browser on `https://miro.com`. We captured 55 unique cookies and 74 external servers before touching the consent banner (`baseline.json` & `pre_consent.png`), and then captured the 10 brand-new cookies that fired immediately after clicking "Accept All" (`post_consent.json` & `post_consent.png`), bringing the total to 65 cookies. We normalized all 301 records into `normalized_evidence.json` with SHA-256 cryptographic fingerprints.
3. **Step 3 (The Initial Sorting):** An automated engine grouped the 301 raw records into 5 candidate activities (Advertising, Analytics, Session/Security, Customer Support, Unclassified). Crucially, the machine left the legal conclusion as `None` because only a qualified human can apply the law.
4. **Step 4 (The Audit Truth Check):** We compared what the website actually did against Miro's official Privacy Policy and Subprocessor list. We discovered that Miro disclosed Intercom and OpenAI, but **failed to disclose Tapad, Reddit, Spotify, Hotjar, and Microsoft Clarity**! We also created a complete 65-cookie inventory register (`COOKIE_VENDOR_INVENTORY.md`).
5. **Step 5 (The Legal Regulatory Filing):** We acted as the Data Protection Officer (DPO) and built the official **Article 30 RoPA** (`ROPA_ARTICLE_30_REGISTER.xlsx`), assigning proper lawful bases under GDPR Art 6 and Indian DPDPA Sec 6/7, cross-border transfer mechanisms (SCCs/DPF), and retention periods.
6. **Step 6 (The High-Risk Warning):** Because Miro runs Microsoft Clarity (screen replay) and Tapad (device tracking), we triggered a formal **Data Protection Impact Assessment (DPIA)** under GDPR Article 35. We proved that Clarity fired in a pre-consent state, creating a severe regulatory violation.
7. **Step 7 (The Commercial Shield):** We wrote the **Vendor DPA Redline Playbook** (`VENDOR_DPA_REDLINE_PLAYBOOK.md`). We took standard vendor click-wrap terms and aggressively redlined them under GDPR Article 28 to forbid vendors from using our telemetry to train their AI models and to mandate a 48-hour breach notification SLA.

---

## 🎓 How to Study This at Your Own Pace

1. Start by reading `00_STUDY_GUIDES_GDPR_DPDPA\PRIVACY_MASTER_TEXTBOOK_GDPR_DPDPA.md` to get comfortable with the law (GDPR articles, DPDPA sections, global principles).
2. Open each folder from `01` to `07` one by one. In every folder, open its `README_STEP...md` first—it tells you in simple words what the files are and what they mean.
3. Open `05_STEP5_ARTICLE_30_ROPA_REGISTER\ROPA_ARTICLE_30_REGISTER.xlsx` in Microsoft Excel to see how enterprise privacy teams present RoPAs.
4. Open `07_STEP7_VENDOR_DPA_REDLINE_PLAYBOOK\VENDOR_DPA_REDLINE_PLAYBOOK.md` to learn how vendor contracts are negotiated.
