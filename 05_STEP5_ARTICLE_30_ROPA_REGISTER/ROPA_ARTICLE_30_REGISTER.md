# 🏛️ STATUTORY RECORDS OF PROCESSING ACTIVITIES (RoPA) REGISTER
### *Enterprise Compliance Documentation under GDPR Article 30 & DPDPA 2023 Section 8*
**Organization:** RealtimeBoard Inc. d/b/a Miro (Delaware, USA) & RealtimeBoard B.V. (Amsterdam, Netherlands)  
**Appointed DPO Contact:** `privacy@miro.com` | Singel 540, 1017 AZ Amsterdam, Netherlands  
**Audit Reference:** `miro_live_audit_run_001` | **Date Certified:** 24 September 2026  
**Verification Base:** [normalized_evidence.json](file:///C:/Users/acer/Downloads/privacy_engineering_real_collection/privacy_engineering_real_collection/runs/miro_audit/normalized_evidence.json) (301 Deterministic SHA-256 Telemetry Records)  
**Associated Excel Workbook:** [ROPA_ARTICLE_30_REGISTER.xlsx](file:///C:/Users/acer/Downloads/privacy_engineering_real_collection/privacy_engineering_real_collection/runs/miro_audit/ROPA_ARTICLE_30_REGISTER.xlsx)

---

## 1. Executive Governance & Legal Scope

Under **GDPR Article 30(1)** and **India's Digital Personal Data Protection Act (DPDPA) 2023 Section 8**, data controllers are legally obligated to maintain an immutable, detailed record of all personal data processing activities under their responsibility.

This register bridges **live frontend network telemetry** captured via automated browser instrumentation with **authoritative legal classifications**, documenting:
1. Exact operational purposes and corresponding statutory lawful bases.
2. Categories of data subjects and personal data elements processed.
3. Third-party recipients, cloud subprocessors, and cross-border international transfer safeguards (Standard Contractual Clauses / DPF).
4. Retention schedules and Technical and Organisational Measures (TOMs) under GDPR Article 32.
5. Mandatory Data Protection Impact Assessment (DPIA) triggers.

---

## 2. Master Article 30 Processing Activities Register

### 📌 [ROPA-ACT-001] Digital Advertising, Retargeting & Conversion Attribution
* **Candidate Telemetry Reference:** `CAND-ACT-E9A99D0D` (41 Supporting Cryptographic Evidence Records)
* **Data Controller:** RealtimeBoard Inc. d/b/a Miro (US) & RealtimeBoard B.V. (EU)
* **Data Protection Officer (DPO):** privacy@miro.com (Amsterdam, Netherlands)
* **Operational Business Purpose:** Delivering targeted digital advertisements, tracking marketing campaign conversion efficacy, and remarketing to visitors across third-party ad networks (Google, LinkedIn, YouTube).
* **Lawful Basis (GDPR Art. 6):** **Article 6(1)(a) - Freely given, specific, informed, and unambiguous Consent**
* **Lawful Basis (DPDPA 2023):** **Section 6(1) - Consent of the Data Principal**
* **Categories of Data Subjects:** Public website visitors, prospective business customers, returning platform users
* **Categories of Personal Data:** Online identifiers (Google DoubleClick 'IDE' cookie, LinkedIn 'bcookie'/'bscookie', Google Click ID 'gclid'), Client IP address, User-Agent browser fingerprint, URL referrer, Timestamp, Ad interaction telemetry
* **Special Category Data (Art. 9):** None collected or inferred
* **Recipients & Cloud Subprocessors:** Google LLC (DoubleClick / Ads, USA), LinkedIn Corporation / LinkedIn Ireland Unlimited Company, Tapad Inc. (USA)
* **Cross-Border Transfers & Safeguards:** USA & Ireland (Third countries). Safeguard: EU Standard Contractual Clauses (SCCs 2021/914 Module 2/3) and EU-US Data Privacy Framework (DPF) certified.
* **Retention Schedule:** Ad tracking cookies: 90 days to 13 months maximum. Aggregated campaign conversion metrics: 24 months.
* **TOMs (Art. 32 Security Measures):** Enforced Pre-Consent gate via OneTrust CMP; TLS 1.3 encryption in transit; SHA-256 pseudonymous identifier hashing; access restricted via corporate SSO/MFA.
* **DPIA Requirement Trigger:** **YES (High Risk due to systematic cross-site tracking and behavioral profiling across ad exchanges)**
* **Audit & Governance Status:** **`REQUIRES LEGAL ACTION (Google DoubleClick & LinkedIn tracking active; Tapad cross-device sync undisclosed in Subprocessor list)`**
* **Sample Cryptographic Evidence IDs:** `EVD-WEB-113-EFD6DA7DD7, EVD-WEB-112-528146B09C, EVD-WEB-027-562EE0EB49`

---
### 📌 [ROPA-ACT-002] Web Traffic Analytics, Audience Measurement & Telemetry
* **Candidate Telemetry Reference:** `CAND-ACT-975E87D5` (50 Supporting Cryptographic Evidence Records)
* **Data Controller:** RealtimeBoard Inc. d/b/a Miro (US) & RealtimeBoard B.V. (EU)
* **Data Protection Officer (DPO):** privacy@miro.com (Amsterdam, Netherlands)
* **Operational Business Purpose:** Aggregating website visit statistics, bounce rates, navigation flow, feature engagement, and technical telemetry to optimize website performance and user experience.
* **Lawful Basis (GDPR Art. 6):** **Article 6(1)(a) - Consent (e-Privacy Directive Art 5(3) & GDPR Art 6(1)(a))**
* **Lawful Basis (DPDPA 2023):** **Section 6(1) - Consent of the Data Principal**
* **Categories of Data Subjects:** Website visitors, prospective registered users
* **Categories of Personal Data:** Google Analytics Client ID ('_ga', '_ga_FK1CGSZNDB'), Segment anonymous ID ('ajs_anonymous_id'), Hotjar session identifier ('_hjSessionUser_763128'), truncated IP, screen resolution, operating system
* **Special Category Data (Art. 9):** None collected or inferred
* **Recipients & Cloud Subprocessors:** Google LLC (Google Analytics 4, USA), Twilio / Segment Inc. (USA), Hotjar Ltd (Malta / EU)
* **Cross-Border Transfers & Safeguards:** USA & Malta. Safeguard: EU Standard Contractual Clauses (SCCs) and adequacy / DPF framework.
* **Retention Schedule:** Google Analytics 4 data retention set to 14 months; Hotjar user identifiers retained up to 365 days; session cookies expire on browser close.
* **TOMs (Art. 32 Security Measures):** Google Analytics IP Anonymization enabled; TLS 1.3 in-transit encryption; OneTrust category classification under 'Performance / Analytics'.
* **DPIA Requirement Trigger:** **NO (Standard web analytics with IP anonymization, provided keystroke/screen replay is sanitized)**
* **Audit & Governance Status:** **`COMPLIANT WITH DISCLOSURE GAP (Google Looker disclosed in Subprocessor PDF, but Hotjar omitted from July 2026 subprocessor list)`**
* **Sample Cryptographic Evidence IDs:** `EVD-WEB-056-D2832FE2EA, EVD-WEB-055-4EA077D761, EVD-WEB-039-9F98B6C691`

---
### 📌 [ROPA-ACT-003] Core Application Session, Security & Consent Management
* **Candidate Telemetry Reference:** `CAND-ACT-625DEF79` (141 Supporting Cryptographic Evidence Records)
* **Data Controller:** RealtimeBoard Inc. d/b/a Miro (US) & RealtimeBoard B.V. (EU)
* **Data Protection Officer (DPO):** privacy@miro.com (Amsterdam, Netherlands)
* **Operational Business Purpose:** Maintaining basic website operation, load balancing, DDoS attack mitigation, bot detection, feature flagging, and recording statutory user consent choices.
* **Lawful Basis (GDPR Art. 6):** **Article 6(1)(f) - Legitimate Interests (Ensuring network and information security, platform availability, and GDPR Article 7 consent compliance)**
* **Lawful Basis (DPDPA 2023):** **Section 7(a) - Legitimate Uses / Necessary operational purposes**
* **Categories of Data Subjects:** All website visitors without exception
* **Categories of Personal Data:** Session tokens, OneTrust consent preference string ('OptanonConsent'), Cloudflare bot mitigation token ('__cf_bm'), server experiment tokens ('server_experiment_viewed'), IP address
* **Special Category Data (Art. 9):** None
* **Recipients & Cloud Subprocessors:** Cloudflare, Inc. (USA), OneTrust LLC (USA / UK), Amazon Web Services (AWS, USA/EU hosting)
* **Cross-Border Transfers & Safeguards:** USA & EU. Safeguard: EU Standard Contractual Clauses (SCCs) & Adequacy.
* **Retention Schedule:** Strictly necessary session cookies: duration of browser session. Consent preference cookie ('OptanonConsent'): 12 months.
* **TOMs (Art. 32 Security Measures):** Strictly necessary category; exempt from prior consent under ePrivacy Directive Art 5(3); Cloudflare automated WAF rate limiting; end-to-end HTTPS TLS 1.3.
* **DPIA Requirement Trigger:** **NO (Essential operational and security telemetry)**
* **Audit & Governance Status:** **`FULLY COMPLIANT (Properly documented, strictly necessary basis justified under Legitimate Interests)`**
* **Sample Cryptographic Evidence IDs:** `EVD-WEB-011-FA171931E3, EVD-WEB-012-7F782573A0, EVD-WEB-001-CDEB879188`

---
### 📌 [ROPA-ACT-004] In-App Customer Support & Conversational Assistance
* **Candidate Telemetry Reference:** `CAND-ACT-E01DEC6E` (2 Supporting Cryptographic Evidence Records)
* **Data Controller:** RealtimeBoard Inc. d/b/a Miro (US) & RealtimeBoard B.V. (EU)
* **Data Protection Officer (DPO):** privacy@miro.com (Amsterdam, Netherlands)
* **Operational Business Purpose:** Providing real-time technical and sales chat support to visitors, routing customer queries, and maintaining ticket continuity across browsing sessions.
* **Lawful Basis (GDPR Art. 6):** **Article 6(1)(b) - Performance of a Contract / Pre-contractual steps at request of data subject, and Article 6(1)(f) Legitimate Interests**
* **Lawful Basis (DPDPA 2023):** **Section 6(1) - Consent / Specified purpose of user engagement**
* **Categories of Data Subjects:** Website visitors actively interacting with the support widget, sales prospects
* **Categories of Personal Data:** Intercom device identifier ('intercom-device-id-fsupkyat'), session identifier ('intercom-session-fsupkyat'), visitor ID ('intercom-id-fsupkyat'), chat message content, timestamps
* **Special Category Data (Art. 9):** None (Chat guardrails prevent submission of sensitive data)
* **Recipients & Cloud Subprocessors:** Intercom, Inc. (USA - Customer support infrastructure)
* **Cross-Border Transfers & Safeguards:** USA. Safeguard: EU Standard Contractual Clauses (SCCs 2021/914) & DPA with Intercom, Inc.
* **Retention Schedule:** Support session cookies: 9 months. Chat transcripts: 24 months in customer CRM, unless deletion requested.
* **TOMs (Art. 32 Security Measures):** Intercom SOC 2 Type II certified; TLS 1.3 encrypted websocket communication; data at rest encrypted via AES-256.
* **DPIA Requirement Trigger:** **NO (Standard enterprise customer support channel)**
* **Audit & Governance Status:** **`DOCUMENTED & DISCLOSED (Intercom, Inc. is explicitly listed in Miro's official July 2026 Subprocessor List)`**
* **Sample Cryptographic Evidence IDs:** `EVD-WEB-048-A73DAC25C6, EVD-WEB-049-1BBF093E51, EVD-WEB-050-D43AC9B9E3`

---
### 📌 [ROPA-ACT-005] Behavioral Session Recording, B2B Lead Enrichment & Shadow Telemetry
* **Candidate Telemetry Reference:** `CAND-ACT-6BF44E43` (67 Supporting Cryptographic Evidence Records)
* **Data Controller:** RealtimeBoard Inc. d/b/a Miro (US) & RealtimeBoard B.V. (EU)
* **Data Protection Officer (DPO):** privacy@miro.com (Amsterdam, Netherlands)
* **Operational Business Purpose:** Replaying user session interactions (mouse movements, clicks, scrolling via Microsoft Clarity), identifying enterprise B2B company domains (Marketo Munchkin / Insightera), and syncing ad audiences (Reddit, Spotify, Facebook, Bing).
* **Lawful Basis (GDPR Art. 6):** **Article 6(1)(a) - Requires Explicit Consent (HIGH RISK OF NON-COMPLIANCE: Currently firing PRE-CONSENT)**
* **Lawful Basis (DPDPA 2023):** **Section 6(1) - Consent of the Data Principal**
* **Categories of Data Subjects:** Website visitors, prospective B2B corporate buyers
* **Categories of Personal Data:** Session replay telemetry (Microsoft Clarity 'CLID', 'MUID', 'ANONCHK'), Marketo tracking ('AWSALBCORS', '_mkto_trk'), Facebook pixel ('fr'), Bing tracking ('MR', 'SRM_B'), cross-network identifiers
* **Special Category Data (Art. 9):** Potential exposure to entered text / form field entries during session recording if masking fails
* **Recipients & Cloud Subprocessors:** Microsoft Corporation (Clarity, USA), Adobe / Marketo Inc. (USA), Meta Platforms Ireland / Facebook Inc., Reddit Inc. (USA), Spotify USA Inc.
* **Cross-Border Transfers & Safeguards:** USA. Safeguard: Requires verified SCCs and Vendor Data Processing Agreements (DPAs).
* **Retention Schedule:** Clarity session recordings: 30 days to 13 months. Marketo cookies: 2 years.
* **TOMs (Art. 32 Security Measures):** Clarity client-side text masking enabled; HTTPS encryption in transit; however, Pre-Consent script blocking was NOT observed for Microsoft Clarity and Marketo.
* **DPIA Requirement Trigger:** **YES (MANDATORY DPIA under GDPR Art 35(3)(a) due to systematic behavioral monitoring and session replay)**
* **Audit & Governance Status:** **`CRITICAL AUDIT FINDING (Pre-consent firing violation + Undisclosed Subprocessors in official July 2026 notice: Clarity, Reddit, Spotify, Marketo)`**
* **Sample Cryptographic Evidence IDs:** `EVD-WEB-017-D94CC7451C, EVD-WEB-041-389D98C946, EVD-WEB-030-DDD2C6CB6A`

---
## 3. Third-Party Subprocessor & International Transfer Matrix

| Subprocessor Legal Name | Processing Activity Mapped | Service Function | Jurisdiction | Transfer Mechanism | Miro Subprocessor List Status | Consent Gate Finding |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **OneTrust LLC** | `ROPA-ACT-003` | Consent Management Platform | USA / UK | Adequacy & SCCs | ✅ Disclosed | **Compliant** (Fires Pre-Consent to log choices) |
| **Cloudflare, Inc.** | `ROPA-ACT-003` | DDoS Protection & Bot Mitigation | USA / Global | SCCs (Module 2/3) | ✅ Disclosed | **Compliant** (Strictly necessary security token) |
| **Intercom, Inc.** | `ROPA-ACT-004` | Real-time Helpdesk & Chat | USA | SCCs 2021/914 | ✅ Disclosed (July 2026) | **Observed Pre-Consent** (Functional) |
| **Google LLC (GA4)** | `ROPA-ACT-002` | Web Audience Analytics | USA | EU-US DPF & SCCs | ⚠️ Looker Disclosed | **Requires Review** (Fires prior to opt-in) |
| **Google LLC (DoubleClick)** | `ROPA-ACT-001` | Ad Remarketing & Conversion | USA | EU-US DPF & SCCs | ⚠️ DoubleClick Omitted | **Compliant Gate** (Held back until Accept All) |
| **LinkedIn Corporation** | `ROPA-ACT-001` | B2B Retargeting & Attribution | Ireland / USA | SCCs 2021/914 | ❌ **Omitted from Subprocessors** | **Violation** (`bcookie` fires Pre-Consent) |
| **Hotjar Ltd** | `ROPA-ACT-002` | Session Heatmaps & Replay | Malta (EU) | EU Internal / EEA | ❌ **Omitted from Subprocessors** | **Violation** (Fires Pre-Consent) |
| **Microsoft Corp (Clarity)** | `ROPA-ACT-005` | Screen Replay & Behavioral Telemetry | USA | SCCs | ❌ **Clarity Omitted** | **CRITICAL Violation** (Fires Pre-Consent; Mandatory DPIA) |
| **Tapad, Inc.** | `ROPA-ACT-001` | Cross-Device Identity Sync | USA | Unverified | ❌ **Undisclosed Shadow Tracker** | **Violation** (Fires Pre-Consent without legal basis) |
| **Adobe / Marketo Inc.** | `ROPA-ACT-005` | B2B Marketing Automation | USA | EU-US DPF & SCCs | ❌ **Omitted from Subprocessors** | **Violation** (Munchkin tracking fires Pre-Consent) |

---

## 4. Remediation Action Plan for Legal & Engineering Teams

1. **Immediate CMP Tag Manager Lockdown:**
   - Configure OneTrust to strictly withhold Microsoft Clarity (`clarity.ms`), Hotjar (`hotjar.com`), Tapad (`tapad.com`), and LinkedIn tracking scripts until explicit user opt-in (`C0002` - Performance, `C0004` - Targeting) is received.
2. **Subprocessor Disclosure Synchronization:**
   - Update Miro's public Subprocessor List PDF to include Hotjar Ltd, LinkedIn Ireland, Microsoft Clarity, and Adobe/Marketo.
3. **Execution of Vendor Data Processing Agreements (DPAs):**
   - Execute formal DPAs featuring EU Standard Contractual Clauses (Module 2 Controller-to-Processor) with Tapad, Inc. and Reddit, Inc.
4. **Initiation of Mandatory DPIA:**
   - Execute Step 6 DPIA Screening on Microsoft Clarity due to automated screen recording and user cursor telemetry.
