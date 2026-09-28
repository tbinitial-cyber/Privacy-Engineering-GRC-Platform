# 🛡️ Privacy Engineering & Comparative Telemetry GRC Research Platform

> **A reproducible privacy-engineering research prototype demonstrating cross-jurisdiction consent management analysis. Combines client-side telemetry capture (Playwright CDP) with evidence hashing, schema validation, and a comparative EU/India consent experiment on Miro.com.**
>
> ⚠️ **Research Prototype Notice:** This is an audit-methodology demonstration, not a certified compliance audit or legal advice. Legal conclusions require qualified legal counsel. Evidence is gathered with a heuristic Evidence Support Index and an append-only DPO review workflow — not a statistically calibrated scoring engine.

[![Statutory Framework](https://img.shields.io/badge/Statutory%20Framework-EU%20GDPR%20%7C%20India%20DPDPA%202023%20%7C%20US%20CCPA-0A66C2.svg)](#-regulatory--statutory-alignment)
[![RoPA Governance](https://img.shields.io/badge/RoPA%20Governance-GDPR%20Art.%2030%20%7C%20DPDPA%20Sec.%208%20Inventory-2ea44f.svg)](#-step-5-statutory-article-30-ropa-register)
[![EDPB WP 248](https://img.shields.io/badge/EDPB%20WP%20248-DPIA%20Screened%20(Regulatory%20Presumption)-critical.svg)](#-step-6-high-risk-dpia-threshold-assessment)
[![Evidence Integrity](https://img.shields.io/badge/Evidence%20Integrity-SHA--256%20Cryptographic%20Fingerprints-blueviolet.svg)](#-step-2-live-digital-telemetry--consent-gate-audit)
[![License](https://img.shields.io/badge/License-MIT-informational.svg)](LICENSE)

---

## Executive Summary

Modern enterprise web platforms deploy sophisticated Consent Management Platforms (CMPs) that dynamically adjust their consent interfaces, cookie storage, and tracking scripts depending on the visitor's geographic location. Evaluating client-side compliance without accounting for this regional variability produces flawed audits—either misapplying EU GDPR standards to non-EU traffic, or overlooking cross-border divergences in data protection controls.

The **Enterprise Privacy Engineering & Dual-Domain Telemetry GRC Platform** bridges technical browser DevTools Protocol (CDP) telemetry with statutory legal compliance. The platform features an empirical **Dual-Jurisdiction Comparative Engine** contrasting real-world telemetry captured under a **European Union benchmark condition (France)** against an **Indian domestic baseline condition**.

---

### Core Empirical Finding: Jurisdiction-Dependent Consent Configuration Observed

Across controlled, clean-slate Chromium sessions on the audited production platform (`https://miro.com`), the web platform exhibited materially divergent consent-management and client-side telemetry behavior based on detected visitor geography:

```
                                  Target: miro.com
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
         🇪🇺 MIRO-EU-001                                  🇮🇳 MIRO-IN-001
      France / Île-de-France                          India / Delhi Baseline
     OneTrust Strict Prior Opt-In                    OneTrust Notice / Opt-Out Style
                 │                                               │
    ├─ Active Groups: ,C0001,                       ├─ Active Groups: ,C0001,C0002,C0003,C0004,C0007,
    ├─ Pre-Consent Cookies: 7                       ├─ Pre-Consent Cookies: 60 (Temporal variation vs earlier 55)
    ├─ Pre-Consent Ad Trackers: 0                   ├─ Pre-Consent Ad Trackers: Firing (Clarity, Tapad)
    ├─ First-Layer Reject All: "Tout refuser"       ├─ First-Layer Reject All: Yes (Observed in latest capture)
    ├─ Post-Reject: 8 cookies (Clean State)         ├─ Post-Reject: 59 cookies
    └─ Post-Accept: 18 cookies                      └─ Post-Accept: 61 cookies
```

*Observation Caveat:* Multiple India captures over a 3-day window demonstrated temporal configuration variability (India pre-consent cookies fluctuated from 55 on Sept 24 to 60 on Sept 27, and a First-Layer Reject All button appeared in the latest run). The platform highlights this configuration variance as an important empirical finding.

---

### Key Comparative Metrics (Audited Platform: Miro Enterprise)

| Forensic Dimension | 🇪🇺 European Union Route (`MIRO-EU-001`) | 🇮🇳 India Route (`MIRO-IN-001`) | Technical & Governance Assessment |
| :--- | :--- | :--- | :--- |
| **Observed GeoIP** | `FR / GES` (`Europe/Paris`) via native VPN | `IN / DL` (`Asia/Kolkata`) direct IP | Intercepted OneTrust GeoIP endpoint (`geolocation.onetrust.com`). 100% Native test contexts. |
| **CMP Active Groups** | `window.OnetrustActiveGroups = ",C0001,"` | `window.OnetrustActiveGroups = ",C0001,C0002,C0003,C0004,C0007,"` | Prior opt-in enforced on EU route; notice/opt-out configuration on domestic route. |
| **First-Layer Banner UX** | Equal prominence: **"Tout refuser"** alongside **"Autoriser"** | Banner included **"Reject All"** in the latest capture (absent in previous) | Varied choice architecture across runs on domestic route under India CPA 2019 Dark Patterns scrutiny. |
| **Pre-Consent Cookies** | **7 Cookies** *(Category C0001 active; cookie-level purpose classification under review)* | **60 Cookies** *(Marketing, analytics & cross-site trackers deposited on load)* | Data minimization observed on European route relative to domestic baseline. |
| **Pre-Consent Ad Trackers** | **0 Known Trackers** *(Clarity, Tapad, DoubleClick withheld during observation window)* | **Active Trackers Firing** *(Microsoft Clarity, Tapad, Hotjar transmit immediately)* | Pre-consent cookie deposition and tracker firing observed on domestic route before affirmative user interaction. Assessed under Indian framework (DPDPA 2023 Sec. 6 / CPA 2019); EU ePrivacy Directive applies to EU route only. |
| **Post-Reject State** | **8 Cookies** *(Clean rejection preserved; +1 preference cookie)* | **59 Cookies** | Proves one-click rejection control is operational in EU. |
| **Post-Accept State** | **18 Cookies** *(Affirmative consent releases analytics/ad cookies)* | **61 Cookies** *(Consent yields parity with baseline + slight variance)* | Demonstrates conditional script-blocking works, but is dynamically relaxed on domestic route. |
| **Applicable Law** | **Observed France/EU consent configuration and client-side behavior relevant to GDPR consent and ePrivacy Article 5(3) assessment.** | **DPDPA 2023 §6** *(Phased commencement)* & **Consumer Protection Act, 2019 / CCPA Dark Patterns Guidelines** | Prospective DPDPA risk once Section 6 phased commencement schedule completes. |

---

## End-to-End Governance Architecture

```mermaid
flowchart TD
    subgraph CaptureLayer ["Multi-Jurisdiction Telemetry Capture (CDP / Playwright)"]
        A1["🇪🇺 EU France Profile (MIRO-EU-001)<br/>Strict Prior Opt-In Verification"]
        A2["🇮🇳 India Domestic Profile (MIRO-IN-001)<br/>Notice-Only Baseline Verification"]
    end

    subgraph IntegrityLayer ["Cryptographic Integrity & Schema Enforcement"]
        B1["Canonical Schema (evidence.schema.json)<br/>Runtime jsonschema validation across all records"]
        B2["Audit Manifest (audit_manifest.json)<br/>Real-time uncached SHA-256 fingerprint verification"]
        B3["Comparative Engine (comparative_analysis.json)<br/>Structured 4-quadrant symmetric delta analysis"]
    end

    subgraph DiscrepancyLayer ["Algorithmic Discovery & Reconciliation"]
        C1["Clustering Engine (Candidate Activities)<br/>70/100 Single-Source | 75/100 Multi-Vector"]
        C2["DPO Append-Only Cryptographic Ledger<br/>Hash-chained append-only event log (no record deletion)"]
        C3["Dual-Domain Transparency Reconciliation<br/>Technical telemetry vs published subprocessor PDFs"]
    end

    subgraph StatutoryLayer ["Statutory Legal Governance"]
        D1["GDPR Article 30 RoPA Register (Statutory)<br/>+ DPDP-Aligned Governance Inventory (Sec. 8 best practice)"]
        D2["EDPB WP 248 High-Risk Screening Note<br/>2 Triggered + 3 Evidence-Supported = 5 of 9 total (Regulatory Presumption)"]
        D3["Vendor DPA Playbook & 10-Provider Benchmark<br/>Contract redlines (48h breach SLA, AI training ban)"]
    end

    CaptureLayer --> IntegrityLayer
    IntegrityLayer --> DiscrepancyLayer
    DiscrepancyLayer --> StatutoryLayer
```

---

## Detailed Step-by-Step Methodology

### 📐 Step 1: Canonical Audit Schema ([`evidence.schema.json`](01_STEP1_CANONICAL_SCHEMA/evidence.schema.json))
- **Mathematical Specification:** Defines strict JSON schema constraints for all ingested evidence records, including `audit_run_id`, `jurisdiction` (`INDIA`, `EU`, `US`), `applicable_framework` (`GDPR`, `DPDPA`), and `geo_context`.
- **Runtime Enforcement:** In [`app.py`](app.py), `jsonschema.validate()` validates every evidence record upon loading.

### 🌐 Step 2: Standardized Multi-Jurisdiction Capture CLI ([`capture_miro.py`](capture_miro.py))
- **Reproducible Instrumentation:** Playwright Chromium script supporting both regional profiles:
  ```bash
  # Both profiles support --action baseline | accept | reject
  # Both use canonical https://miro.com/ as initial URL (geography is the sole variable)

  python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809 --action baseline
  python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809 --action accept
  python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809 --action reject

  python capture_miro.py --profile india --action baseline
  python capture_miro.py --profile india --action accept
  python capture_miro.py --profile india --action reject
  ```
- **Captured Fields:** OneTrust GeoIP response, DOM-level `window.OnetrustActiveGroups`, full HTTP Archive (HAR), pre-consent cookies, post-action cookies (Accept All / Reject All), initial_url / final_url (redirect chain). Network event stream captures URL, method, resource_type, and timestamp; full Set-Cookie / response-header forensics are captured in the HAR.

### 🧩 Step 3: Algorithmic Discovery & Append-Only DPO Governance
- **Evidence Support Index (Heuristic — Not a Probability):**
  - **70/100 (Single-Source):** Activity inferred from a single technical discovery layer (e.g., HTTP Network Traffic only).
  - **75/100 (Multi-Vector Corroboration):** Activity corroborated across multiple independent layers (e.g., confirmed in both active CDP network beacon *and* persistent DOM cookie storage).
  - **Calibration Note:** These values are ordinal/heuristic scores indicating technical corroboration depth. They are NOT statistically calibrated probabilities and do not constitute legal conclusions. Human DPO/Legal Counsel review is required for all governance decisions.
- **Append-Only Event Ledger ([`dpo_signoff_log.json`](03_STEP3_CANDIDATE_ACTIVITIES/dpo_signoff_log.json)):**
  - Uses an append-only, cryptographically chained event log (`SIGNOFF_RECORDED`, `SIGNOFF_REVOKED`). Each event is SHA-256 linked to the prior event hash; no historical records are deleted or mutated.
  - Never mutates or deletes historical sign-off records; active state is derived chronologically.
  - Human validation adds `dpo_review_status = APPROVED` without falsely inflating the technical support score.

### 🔍 Step 4: Dual-Domain Discrepancy & Transparency Reconciliation
- **Ground Truth vs. Public Disclosures:** Cross-references observed network destinations against Miro's public Subprocessor List PDF (July 2026).
- **Discovered Shadow Telemetry:** Identified unlisted third-party trackers including **Microsoft Clarity** (`CLID`, `SM`, `MUID`), **Tapad Inc.** (`TapAd_3WAY_SYNCS`), and **Hotjar** actively communicating with external infrastructure.

### 🏛️ Step 5: Multi-Jurisdictional RoPA Register ([`ROPA_ARTICLE_30_REGISTER.md`](04_STEP4_TRANSPARENCY_AND_COOKIE_REGISTER/ROPA_ARTICLE_30_REGISTER.md))
- **GDPR Article 30 RoPA (Statutory):** Statutory Record of Processing Activities for Data Controllers.
- **DPDP-Aligned Governance Inventory (Operational):** DPDPA 2023 does not establish a statutory RoPA requirement. This platform maintains a separate DPDP-aligned processing inventory as an organizational best practice under Section 8 accountability duties — distinct from the GDPR Art. 30 statutory register.

### 🛡️ Step 6: High-Risk DPIA Threshold Assessment ([`DPIA_SCREENING_NOTE.md`](06_STEP6_DPIA_SCREENING_NOTE/DPIA_SCREENING_NOTE.md))
- **EDPB Guidelines WP 248 rev.01:** Evaluates live telemetry against the 9 supervisory criteria.
- **5 of 9 Criteria Triggered or Evidence-Supported:** 2 directly triggered (Systematic Monitoring via Clarity DOM replay, Large Scale), 3 evidence-supported (Profiling/Tapad sync identifiers, Dataset Combination, Innovative Technology). Evidence-supported criteria are consistent with the criterion but require further investigation beyond cookie observation.
- **Regulatory Verdict:** Triggers a strong regulatory presumption in supervisory guidance warranting a formal Data Protection Impact Assessment under GDPR Article 35(1).

### 📑 Step 7: Vendor DPA Contract Redline Playbook & 10-Provider Benchmark
- **7 Battleground Contract Redlines:** 48-hour breach notification SLA, strict AI model training prohibition, 30-day subprocessor veto window, and direct audit rights.
- **Cross-Industry Scorecard:** 10-point comparative analysis across AWS, GCP, Azure, Salesforce, Atlassian, Stripe, HubSpot, Cloudflare, Freshworks, and Zoho.

---

## 🏛️ Statutory Alignment Summary

| Statute / Instrument | Specific Section | Governance Application |
| :--- | :--- | :--- |
| **EU GDPR** | **Arts. 4(11), 6(1)(a)** (Valid Consent) | Observed consent configuration on EU route consistent with prior opt-in requirements. Art. 7(3) withdrawal lifecycle requires a separate post-consent withdrawal test not conducted in this run. |
| **EU ePrivacy Directive** | **Art. 5(3)** (Terminal Storage Access) | Enforces prior opt-in for non-essential client-side cookies and DOM storage. |
| **EU GDPR** | **Art. 30** (Records of Processing Activities) | Multi-sheet controller inventory with lawful bases, retention rules, and TOMs. |
| **EU GDPR** | **Art. 35(1)** (High-Risk DPIA Screening) | Screened against EDPB WP 248 9-criteria matrix; 5 factors triggered. |
| **EU GDPR** | **Art. 28** (Processor Contract Terms) | Standardized DPA redline playbook with mandatory audit and breach SLAs. |
| **India DPDPA 2023** | **Sec. 6** (Notice & Consent Mandates) | Evaluated prospective compliance for domestic route under phased commencement. |
| **India DPDPA 2023** | **Sec. 8** (Fiduciary Accountability) | Operational processing inventory maintained as organizational governance practice. |
| **Consumer Protection Act 2019 (India)** | **Dark Patterns Guidelines 2023 (India CCPA)** | Scrutinizes omission of first-layer "Reject All" as asymmetric choice architecture (distinguished from California CCPA). |
| **US CCPA / CPRA** | **Cal. Civ. Code § 1798.135** | Identifies cross-context behavioral ad trackers triggering opt-out disclosures (California). |

---

## 🚀 Running the Platform

### Prerequisites
* Python 3.10+
* Google Chrome / Chromium installed via Playwright

### Installation
```bash
git clone https://github.com/tbinitial-cyber/Privacy-Engineering-GRC-Platform.git
cd Privacy-Engineering-GRC-Platform
pip install -r requirements.lock
playwright install chromium
```

### Launch Interactive Executive Portal
```bash
streamlit run app.py
```

### Reproduce Empirical Audit Captures
```bash
# Capture European Union benchmark — baseline, accept, and reject states
python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809 --action baseline
python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809 --action accept
python capture_miro.py --profile eu-france --proxy http://127.0.0.1:61809 --action reject

# Capture Indian Domestic baseline, accept, and reject states
python capture_miro.py --profile india --action baseline
python capture_miro.py --profile india --action accept
python capture_miro.py --profile india --action reject

# NOTE: For causal attribution, run both jurisdictions within the same calendar session window.
```

---

## License
MIT License. Created for privacy engineering research, technical GRC prototyping, and comparative consent-management analysis. This repository is a research prototype and does not constitute legal advice or a certified compliance audit.
