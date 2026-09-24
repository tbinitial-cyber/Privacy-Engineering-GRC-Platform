import streamlit as st
import pandas as pd
import json
import os
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Privacy Engineering & Technical GRC Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-title { font-size: 32px; font-weight: bold; color: #1B365D; margin-bottom: 0px; }
    .sub-title { font-size: 16px; color: #555555; margin-bottom: 20px; }
    .card-metric { background-color: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; padding: 15px; }
    .status-badge-critical { background-color: #FEE2E2; color: #991B1B; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .status-badge-compliant { background-color: #DCFCE7; color: #166534; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
    .status-badge-warning { background-color: #FEF3C7; color: #92400E; padding: 4px 8px; border-radius: 4px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(rel_path):
    # Cross-platform path resolver (replaces Windows backslashes with forward slashes)
    clean_rel = rel_path.replace("\\", "/")
    return os.path.normpath(os.path.join(BASE_DIR, clean_rel))

# Helper to load JSON (no stale cache)
def load_json_file(rel_path):
    full_path = get_path(rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

# Helper to load Markdown (no stale cache)
def load_md_file(rel_path):
    full_path = get_path(rel_path)
    if os.path.exists(full_path):
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
    return "File not found."

# Purge any legacy cache on script reload
st.cache_data.clear()

# Sidebar Navigation
st.sidebar.image("https://img.icons8.com/color/96/shield.png", width=64)
st.sidebar.title("Privacy GRC Pipeline")
st.sidebar.caption("Empirical Telemetry Audit to Statutory Governance")

nav_choice = st.sidebar.radio(
    "GRC Audit Modules:",
    [
        "📊 Executive CISO & DPO Dashboard",
        "🌐 01. Live Telemetry & Consent Gate Audit",
        "🧩 02. Algorithmic Processing Activities",
        "🔍 03. Transparency Reconciliation & Cookies",
        "🏛️ 04. Statutory Article 30 RoPA Register",
        "🛡️ 05. High-Risk DPIA Threshold Assessment",
        "📑 06. Vendor DPA Contract Redline Playbook",
        "🏢 07. Industry DPA Benchmark Scorecard",
        "📜 08. Enterprise Privacy Policy Governance"
    ]
)

st.sidebar.divider()
st.sidebar.info("💡 **Dual-Domain GRC Architecture:** Combining Playwright network packet instrumentation with GDPR Art. 28/30/35, Indian DPDPA 2023 Sec. 8/10 & California CCPA/CPRA.")

# ----------------------------------------------------
# 1. EXECUTIVE DASHBOARD
# ----------------------------------------------------
if nav_choice == "📊 Executive CISO & DPO Dashboard":
    st.markdown('<div class="main-title">🛡️ Privacy Engineering & Technical GRC Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Empirical Live Telemetry Audit of Miro.com | Regulatory Compliance under GDPR, DPDPA 2023 & CCPA/CPRA</div>', unsafe_allow_html=True)
    
    # Top KPI Metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Cryptographic Evidence", value="301 Records", delta="SHA-256 Verified")
    with col2:
        st.metric(label="Unique Cookies Mapped", value="65 Cookies", delta="55 Pre + 10 Post")
    with col3:
        st.metric(label="Discovered External Hosts", value="74 Servers", delta="Network Scanned")
    with col4:
        st.metric(label="Mandatory RoPA Entries", value="5 Activities", delta="GDPR Art 30 / DPDPA")
    with col5:
        st.metric(label="Mandatory DPIA Triggers", value="2 High Risk", delta="Clarity & Tapad", delta_color="inverse")

    st.divider()
    
    # Architecture Overview
    st.subheader("🏛️ Enterprise End-to-End Compliance Lifecycle")
    st.markdown("""
    This platform demonstrates a complete **dual-domain compliance lifecycle** bridging technical browser network packets with statutory corporate governance:
    """)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("### 1. Technical Collection")
        st.markdown("""
        * **Automated Chromium Instrumentation:** Playwright CDP capture.
        * **Consent Gate Verification:** Pre-Consent vs Post-Consent baseline.
        * **Canonical Normalization:** 301 JSON Schema records with deterministic SHA-256 IDs.
        """)
    with c2:
        st.markdown("### 2. Reconciliation & Risk")
        st.markdown("""
        * **Audit Truth Check:** Technical packets vs Miro's Privacy Notice.
        * **Caught 5 Shadow Vendors:** Tapad, Reddit, Spotify, Hotjar, Clarity.
        * **EDPB DPIA Screening:** 4 of 9 criteria met triggering mandatory DPIA.
        """)
    with c3:
        st.markdown("### 3. Statutory Governance")
        st.markdown("""
        * **Article 30 RoPA:** 4-sheet corporate Excel workbook.
        * **Vendor DPA Playbook:** 7 battleground contract redlines.
        * **Benchmark Library:** 10 real-world DPA dissections & public policy.
        """)

    st.info("👈 Use the left sidebar to navigate step-by-step through each verified phase of the audit pipeline.")

# ----------------------------------------------------
# 2. MODULE 01: LIVE TELEMETRY & CONSENT GATE
# ----------------------------------------------------
elif nav_choice == "🌐 01. Live Telemetry & Consent Gate Audit":
    st.header("🌐 Module 01: Live Telemetry Capture & Consent Gate Audit")
    st.caption("Empirical network recording on Miro (https://miro.com) using Playwright Chromium + Chrome DevTools Protocol (CDP)")
    
    tab1, tab2, tab3 = st.tabs(["📸 Pre vs Post Consent Screenshots", "🍪 Cookie State Comparison", "🌐 Network Host Inventory"])
    
    with tab1:
        st.subheader("Visual Consent Gate Verification")
        st.write("Notice how Google DoubleClick (`IDE`) was withheld in the Pre-Consent state, but Microsoft Clarity and Hotjar fired immediately before clicking the banner.")
        col_pre, col_post = st.columns(2)
        
        pre_img_path = get_path("02_STEP2_RAW_AND_NORMALIZED_TELEMETRY/pre_consent.png")
        post_img_path = get_path("02_STEP2_RAW_AND_NORMALIZED_TELEMETRY/post_consent.png")
        
        with col_pre:
            st.markdown("#### 1. Pre-Consent Baseline (Banner Active)")
            if os.path.exists(pre_img_path):
                st.image(pre_img_path, caption="Miro Landing Surface with OneTrust CMP Active (55 Cookies Dropped)", width="stretch")
            else:
                st.warning("Pre-consent screenshot not found.")
                
        with col_post:
            st.markdown("#### 2. Post-Consent State (After 'Accept All')")
            if os.path.exists(post_img_path):
                st.image(post_img_path, caption="Miro Surface after Affirmative Click (+10 New Cookies Released = 65 Total)", width="stretch")
            else:
                st.warning("Post-consent screenshot not found.")

    with tab2:
        st.subheader("The Consent Math: 55 Baseline + 10 Post-Consent = 65 Total Cookies")
        base_data = load_json_file(r"02_STEP2_RAW_AND_NORMALIZED_TELEMETRY/baseline.json")
        post_data = load_json_file(r"02_STEP2_RAW_AND_NORMALIZED_TELEMETRY/post_consent.json")
        
        if base_data and post_data:
            b_cookies = base_data.get("cookies", [])
            p_cookies = post_data.get("cookies", [])
            
            c_m1, c_m2, c_m3 = st.columns(3)
            c_m1.metric("Pre-Consent Cookies", f"{len(set((c['name'], c['domain']) for c in b_cookies))} Unique", "Baseline Storage")
            c_m2.metric("New Cookies Released Post-Consent", "10 Brand New", "Gate Functioning")
            c_m3.metric("Total Post-Consent State", "65 Unique", "Final Inventory")
            
            st.markdown("#### The 10 Brand-New Cookies Released Post-Consent:")
            post_cookies_list = [
                {"Cookie": "IDE", "Domain": ".doubleclick.net", "Vendor": "Google DoubleClick", "Category": "Advertising / Retargeting", "Status": "Properly Gated"},
                {"Cookie": "bscookie", "Domain": ".www.linkedin.com", "Vendor": "LinkedIn Corporation", "Category": "Advertising / Attribution", "Status": "Properly Gated"},
                {"Cookie": "__Secure-YNID", "Domain": ".youtube.com", "Vendor": "Google / YouTube", "Category": "Targeting & Media", "Status": "Properly Gated"},
                {"Cookie": "YSC", "Domain": ".youtube.com", "Vendor": "Google / YouTube", "Category": "Targeting & Media", "Status": "Properly Gated"},
                {"Cookie": "VISITOR_INFO1_LIVE", "Domain": ".youtube.com", "Vendor": "Google / YouTube", "Category": "Targeting & Media", "Status": "Properly Gated"},
                {"Cookie": "VISITOR_PRIVACY_METADATA", "Domain": ".youtube.com", "Vendor": "Google / YouTube", "Category": "Targeting & Media", "Status": "Properly Gated"},
                {"Cookie": "__Secure-ROLLOUT_TOKEN", "Domain": ".youtube.com", "Vendor": "Google / YouTube", "Category": "Targeting & Media", "Status": "Properly Gated"},
                {"Cookie": "__cf_bm", "Domain": ".bzr.openai.com", "Vendor": "Cloudflare / OpenAI", "Category": "Security Bot Mitigation", "Status": "Post-Consent Load"},
                {"Cookie": "_cfuvid", "Domain": ".bzr.openai.com", "Vendor": "OpenAI LLC", "Category": "Functional Telemetry", "Status": "Post-Consent Load"},
                {"Cookie": "AWSALBCORS", "Domain": "nld1rtp1.marketo.com", "Vendor": "Adobe / Marketo", "Category": "B2B Marketing Telemetry", "Status": "Post-Consent Load"}
            ]
            st.table(pd.DataFrame(post_cookies_list))

    with tab3:
        st.subheader("Discovered External Host Inventory (74 Servers)")
        st.caption("All distinct third-party and external endpoints communicating with user browser during page lifecycle.")
        hosts = load_json_file(r"02_STEP2_RAW_AND_NORMALIZED_TELEMETRY/host_inventory.json")
        if hosts:
            df_hosts = pd.DataFrame(hosts)
            
            # Format list of resource types
            if "resource_types" in df_hosts.columns:
                df_hosts["resource_types"] = df_hosts["resource_types"].apply(
                    lambda x: ", ".join(x) if isinstance(x, list) else str(x)
                )
                
            df_hosts = df_hosts.rename(columns={
                "host": "Discovered Host Domain",
                "request_count": "HTTP Request Volume",
                "resource_types": "Observed Resource Payloads"
            })
            
            # Sort by highest request count
            if "HTTP Request Volume" in df_hosts.columns:
                df_hosts = df_hosts.sort_values(by="HTTP Request Volume", ascending=False)
                
            # Quick KPI metrics
            h_c1, h_c2 = st.columns(2)
            with h_c1:
                st.metric("Total Unique Hosts Discovered", f"{len(df_hosts)}")
            with h_c2:
                total_reqs = df_hosts["HTTP Request Volume"].sum() if "HTTP Request Volume" in df_hosts.columns else 0
                st.metric("Total Captured Network Requests", f"{total_reqs} Requests")
                
            # Search filter
            host_search = st.text_input("🔍 Filter host domains (e.g., google, clarity, tapad, reddit):", "")
            if host_search:
                df_hosts = df_hosts[df_hosts.astype(str).apply(lambda x: x.str.contains(host_search, case=False)).any(axis=1)]
                
            st.dataframe(df_hosts, width="stretch", height=450, hide_index=True)
            
            # CSV Download
            csv_hosts = df_hosts.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Discovered Host Inventory (CSV)",
                data=csv_hosts,
                file_name="miro_discovered_host_inventory.csv",
                mime="text/csv"
            )
        else:
            st.warning("Host inventory file not found.")

# ----------------------------------------------------
# 3. MODULE 02: ALGORITHMIC PROCESSING ACTIVITIES
# ----------------------------------------------------
elif nav_choice == "🧩 02. Algorithmic Processing Activities":
    st.header("🧩 Module 02: Algorithmic Processing Activity Clustering")
    st.caption("Heuristic clustering of 301 raw telemetry records into 5 candidate business processing activities")
    
    st.markdown("""
    > 🧠 **Algorithmic Confidence Scoring Architecture (Why 0.70 vs. 0.75?):**
    > * **Single-Source Ingestion (0.70 / 70% Confidence):** Activity is inferred from a single technical discovery layer (e.g., HTTP Network Traffic only or Client Cookie Storage only).
    > * **Multi-Vector Corroboration (0.75 / 75% Confidence):** Activity is corroborated across multiple independent layers (e.g., confirmed both in active CDP Network Beacons AND persistent DOM Cookie Storage).
    > * **The Human-in-the-Loop Cap (<0.80):** In automated privacy engineering, machine algorithms are strictly capped below 0.80. Under GDPR Article 30 and Indian DPDPA Section 8, software cannot declare statutory purpose or legal lawful basis. Full **1.0 (100% Audit-Grade Certainty)** is achieved only upon completing the 8 statutory validation questions during human DPO/Legal review.
    """)
    
    candidates = load_json_file(r"03_STEP3_CANDIDATE_ACTIVITIES/candidate_processing_activities.json")
    if candidates:
        for idx, act in enumerate(candidates, 1):
            conf = act.get('confidence', 0.0)
            sources = act.get('evidence_sources', [])
            conf_label = f"{int(conf * 100)}% (Multi-Vector Corroborated)" if conf > 0.7 else f"{int(conf * 100)}% (Single-Source Ingestion)"
            
            with st.expander(f"📌 Candidate Activity 0{idx}: {act.get('candidate_purpose', 'Unclassified').upper()} | Confidence: {conf_label}"):
                c1, c2 = st.columns(2)
                with c1:
                    st.write(f"**Candidate Activity ID:** `{act.get('candidate_activity_id')}`")
                    st.write(f"**Proposed Business Purpose:** `{act.get('candidate_purpose')}`")
                    st.write(f"**Data Subjects Identified:** `{', '.join(act.get('candidate_data_subjects', []))}`")
                    st.write(f"**Supporting Evidence Count:** {len(act.get('evidence_ids', []))} Cryptographic Records")
                    st.write(f"**Discovery Vectors:** `{', '.join(sources)}`")
                with c2:
                    st.write(f"**Legal Conclusion:** `{act.get('legal_conclusion')}` (Pending Human Review)")
                    st.write(f"**Validation Questions Triggered:** {len(act.get('validation_questions', []))} Statutory Questions")
                    st.markdown("**Sample Discovered Recipients:**")
                    recipients = act.get("candidate_recipients", [])[:5]
                    for r in recipients:
                        st.code(f"{r.get('kind')}: {r.get('identifier')}")
                        
                with st.expander("⚖️ View the 8 Human Validation Questions for DPO Review:"):
                    for q_idx, q in enumerate(act.get("validation_questions", []), 1):
                        st.write(f"**Q{q_idx}:** {q}")

# ----------------------------------------------------
# 4. MODULE 03: TRANSPARENCY RECONCILIATION & COOKIES
# ----------------------------------------------------
elif nav_choice == "🔍 03. Transparency Reconciliation & Cookies":
    st.header("🔍 Module 03: Transparency Reconciliation & Cookie Inventory")
    st.caption("Comparing Technical Reality (Network Packets) against Documented Reality (Privacy Notice & Subprocessor PDF)")
    
    tab_recon, tab_inv = st.tabs(["🚨 Transparency Reconciliation Gotchas", "🍪 65-Cookie Interactive Inventory"])
    
    with tab_recon:
        st.subheader("The Audit 'Gotchas' Table")
        st.caption("Side-by-side reconciliation between captured telemetry packets and Miro's published Privacy Statement & Subprocessor List.")
        st.markdown("""
        | Vendor Discovered | Technical Function | Documented in Miro Notice? | Status / Statutory Finding |
        | :--- | :--- | :---: | :--- |
        | **Intercom, Inc.** | Customer Live Chat | ✅ Disclosed | **Compliant** (Listed in July 2026 Subprocessor PDF) |
        | **OpenAI LLC** | AI Workspace Features | ✅ Disclosed | **Compliant** (Listed in July 2026 Subprocessor PDF) |
        | **Google Analytics** | Audience Measurement | ⚠️ Partial | Disclosed for Looker, but DoubleClick omitted |
        | **Microsoft Clarity** | Session Screen Replay | ❌ **Omitted** | 🚨 **Severe Disclosure Gap** (`c.clarity.ms` active) |
        | **Tapad, Inc.** | Cross-Device Ad Sync | ❌ **Omitted** | 🚨 **Undisclosed Data Broker** (`TapAd_3WAY_SYNCS`) |
        | **Reddit Ad Pixel** | Ad Conversion Beacon | ❌ **Omitted** | 🚨 **Undisclosed Tracker** (`alb.reddit.com`) |
        | **Spotify Ad Pixel**| Ad Retargeting Pixel | ❌ **Omitted** | 🚨 **Undisclosed Tracker** (`pixel.byspotify.com`) |
        | **Hotjar Ltd** | Session Heatmaps | ❌ **Omitted** | 🚨 **Pre-Consent Violation** (`_hjSessionUser`) |
        """)
        
        st.divider()
        st.subheader("📋 Candidate Processing Activities Transparency Reconciliation")
        recon_md = load_md_file(r"04_STEP4_TRANSPARENCY_AND_COOKIE_REGISTER/TRANSPARENCY_RECONCILIATION_REPORT.md")
        st.markdown(recon_md)
        
    with tab_inv:
        st.subheader("Interactive 65-Cookie Register")
        st.caption("Complete mapping of 65 captured cookies across baseline pre-consent and gated post-consent states.")
        
        cookie_inv = load_json_file(r"04_STEP4_TRANSPARENCY_AND_COOKIE_REGISTER/cookie_vendor_inventory.json")
        if cookie_inv:
            df_cookies = pd.DataFrame(cookie_inv)
            
            # Metrics Row
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric("Total Cookies Mapped", f"{len(df_cookies)}")
            with c2:
                pre_count = len(df_cookies[df_cookies.get("consent_state", "") == "PRE_CONSENT"])
                st.metric("Pre-Consent Dropped", f"{pre_count}", delta="Baseline Unauthenticated")
            with c3:
                post_count = len(df_cookies[df_cookies.get("consent_state", "") == "POST_CONSENT"])
                st.metric("Gated Post-Consent", f"{post_count}", delta="+10 Affirmative Release")
            with c4:
                vendor_col = "vendor_owner" if "vendor_owner" in df_cookies.columns else df_cookies.columns[3]
                vendor_count = df_cookies[vendor_col].nunique()
                st.metric("Unique Vendors / Owners", f"{vendor_count}")
                
            st.divider()
            
            # Filter bar
            f_col1, f_col2, f_col3 = st.columns([2, 1, 1])
            with f_col1:
                search = st.text_input("🔍 Search cookies (name, domain, vendor, purpose):", "")
            with f_col2:
                consent_filter = st.selectbox("Consent Filter:", ["All States", "PRE_CONSENT Only", "POST_CONSENT Only"])
            with f_col3:
                cat_col = "category_group" if "category_group" in df_cookies.columns else None
                if cat_col:
                    categories = ["All Categories"] + sorted(list(df_cookies[cat_col].dropna().unique()))
                    cat_filter = st.selectbox("Category Filter:", categories)
                else:
                    cat_filter = "All Categories"
                
            # Apply filters safely
            filtered_df = df_cookies.copy()
            if consent_filter == "PRE_CONSENT Only" and "consent_state" in filtered_df.columns:
                filtered_df = filtered_df[filtered_df["consent_state"] == "PRE_CONSENT"]
            elif consent_filter == "POST_CONSENT Only" and "consent_state" in filtered_df.columns:
                filtered_df = filtered_df[filtered_df["consent_state"] == "POST_CONSENT"]
                
            if cat_filter != "All Categories" and cat_col and cat_col in filtered_df.columns:
                filtered_df = filtered_df[filtered_df[cat_col] == cat_filter]
                
            if search:
                filtered_df = filtered_df[filtered_df.astype(str).apply(lambda x: x.str.contains(search, case=False)).any(axis=1)]
                
            # Presentation mapping
            display_cols = {
                "cookie_name": "Cookie Name",
                "domain": "Domain",
                "vendor_owner": "Vendor / Entity",
                "category_group": "Category",
                "consent_state": "Consent State",
                "purpose_description": "Purpose Description",
                "evidence_id": "Evidence ID"
            }
            
            cols_to_use = [c for c in display_cols.keys() if c in filtered_df.columns]
            table_display = filtered_df[cols_to_use].rename(columns=display_cols)
            
            st.dataframe(table_display, height=450, width="stretch", hide_index=True)
            st.caption(f"Showing {len(table_display)} of {len(df_cookies)} cookies.")
            
            # CSV Download
            csv_data = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Filtered Cookie Register (CSV)",
                data=csv_data,
                file_name="miro_cookie_vendor_register.csv",
                mime="text/csv"
            )
        else:
            st.warning("Cookie inventory JSON file not found.")

# ----------------------------------------------------
# 5. MODULE 04: ARTICLE 30 ROPA REGISTER
# ----------------------------------------------------
elif nav_choice == "🏛️ 04. Statutory Article 30 RoPA Register":
    st.header("🏛️ Module 04: Statutory Records of Processing Activities (RoPA)")
    st.caption("Certified Enterprise Compliance Register under GDPR Article 30(1) & Indian DPDPA 2023 Section 8")
    
    excel_path = get_path("05_STEP5_ARTICLE_30_ROPA_REGISTER/ROPA_ARTICLE_30_REGISTER.xlsx")
    if os.path.exists(excel_path):
        with open(excel_path, "rb") as f:
            st.download_button(
                label="📥 Download Certified Corporate RoPA Workbook (Excel .xlsx)",
                data=f.read(),
                file_name="Miro_RoPA_Article_30_Register.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
    st.divider()
    
    # 5 RoPA Activities
    ropa_summary = [
        {"RoPA ID": "ROPA-ACT-001", "Activity Name": "Digital Advertising & Retargeting", "GDPR Basis": "Art. 6(1)(a) Consent", "DPDPA Basis": "Sec. 6(1) Consent", "DPIA": "YES (High Risk)", "Status": "Action Required (Tapad undisclosed)"},
        {"RoPA ID": "ROPA-ACT-002", "Activity Name": "Web Analytics & Telemetry", "GDPR Basis": "Art. 6(1)(a) Consent", "DPDPA Basis": "Sec. 6(1) Consent", "DPIA": "NO", "Status": "Disclosure Gap (Hotjar omitted)"},
        {"RoPA ID": "ROPA-ACT-003", "Activity Name": "Session Security & Consent", "GDPR Basis": "Art. 6(1)(f) Legitimate Interests", "DPDPA Basis": "Sec. 7(a) Legitimate Uses", "DPIA": "NO", "Status": "Fully Compliant"},
        {"RoPA ID": "ROPA-ACT-004", "Activity Name": "Customer Support Live Chat", "GDPR Basis": "Art. 6(1)(b) Contract", "DPDPA Basis": "Sec. 6(1) Consent", "DPIA": "NO", "Status": "Documented & Disclosed"},
        {"RoPA ID": "ROPA-ACT-005", "Activity Name": "Behavioral Replay & Lead Sync", "GDPR Basis": "Art. 6(1)(a) Consent (Violation)", "DPDPA Basis": "Sec. 6(1) Consent", "DPIA": "YES (MANDATORY)", "Status": "Critical Violation (Pre-Consent firing)"}
    ]
    st.table(pd.DataFrame(ropa_summary))
    
    st.markdown("### Master Processing Activity Details")
    ropa_md = load_md_file(r"05_STEP5_ARTICLE_30_ROPA_REGISTER/ROPA_ARTICLE_30_REGISTER.md")
    with st.expander("📄 View Full Publication-Grade Markdown RoPA Register"):
        st.markdown(ropa_md)

# ----------------------------------------------------
# 6. MODULE 05: DPIA SCREENING & RISK HEATMAP
# ----------------------------------------------------
elif nav_choice == "🛡️ 05. High-Risk DPIA Threshold Assessment":
    st.header("🛡️ Module 05: Data Protection Impact Assessment (DPIA) Screening")
    st.caption("Statutory High-Risk Threshold Assessment under GDPR Article 35 & EDPB Guidelines WP 248")
    
    col_v1, col_v2 = st.columns([1, 2])
    with col_v1:
        st.error("🚨 STATUTORY VERDICT:\n\n**FULL DPIA MANDATORY**\n\n4 of 9 EDPB Criteria Met (Statutory threshold is 2).")
        st.write("**Key Triggers:**")
        st.write("1. Microsoft Clarity Screen Replay (`CLID`, `MUID`)")
        st.write("2. Tapad Cross-Device Graph Sync (`3WAY_SYNCS`)")
        st.write("3. Pre-Consent Firing Violation")
        
    with col_v2:
        st.subheader("EDPB 9-Criteria Threshold Matrix")
        criteria_data = [
            {"Criterion": "1. Evaluation or Scoring (Profiling)", "Status": "TRIGGERED", "Evidence": "Tapad & LinkedIn conversion scoring"},
            {"Criterion": "2. Automated Decision-Making", "Status": "NOT TRIGGERED", "Evidence": "Ad bidding only; no legal effects"},
            {"Criterion": "3. Systematic Monitoring", "Status": "TRIGGERED", "Evidence": "Microsoft Clarity DOM & mouse recording"},
            {"Criterion": "4. Sensitive Data", "Status": "POTENTIAL", "Evidence": "Form field inputs captured if unmasked"},
            {"Criterion": "5. Large Scale", "Status": "TRIGGERED", "Evidence": "Millions of monthly global visitors"},
            {"Criterion": "6. Matching / Combining Datasets", "Status": "TRIGGERED", "Evidence": "Tapad 3-Way Sync cross-device graph"},
            {"Criterion": "7. Vulnerable Subjects", "Status": "NOT TRIGGERED", "Evidence": "B2B SaaS workspace platform"},
            {"Criterion": "8. Innovative Technology", "Status": "TRIGGERED", "Evidence": "Real-time DOM mutation virtualization"},
            {"Criterion": "9. Denying Rights", "Status": "NOT TRIGGERED", "Evidence": "User can theoretically delete cookies"}
        ]
        st.table(pd.DataFrame(criteria_data))

    dpia_md = load_md_file(r"06_STEP6_DPIA_SCREENING_NOTE/DPIA_SCREENING_NOTE.md")
    with st.expander("📄 View Full Statutory DPIA Screening Note"):
        st.markdown(dpia_md)

# ----------------------------------------------------
# 7. MODULE 06: VENDOR DPA REDLINING PLAYBOOK
# ----------------------------------------------------
elif nav_choice == "📑 06. Vendor DPA Contract Redline Playbook":
    st.header("📑 Module 06: Vendor DPA Contract Redlining Playbook")
    st.caption("TPRM Negotiation Guide: Standard Vendor Traps vs. Our Enterprise Privacy Redlines under GDPR Art. 28")
    
    st.info("💼 **The TPRM Shield:** Technical telemetry found the leak; this contract playbook stops commercial exploitation.")
    
    dpa_playbook_md = load_md_file(r"07_STEP7_VENDOR_DPA_REDLINE_PLAYBOOK/VENDOR_DPA_REDLINE_PLAYBOOK.md")
    st.markdown(dpa_playbook_md)

# ----------------------------------------------------
# 8. MODULE 07: 10 DPA BENCHMARK SCORECARD
# ----------------------------------------------------
elif nav_choice == "🏢 07. Industry DPA Benchmark Scorecard":
    st.header("🏢 Module 07: Real-World Enterprise DPA Benchmark Scorecard")
    st.caption("10-Point Technical & Commercial Battleground Analysis across 10 Industry Giants")
    
    scorecard_path = get_path("08_REAL_WORLD_DPA_BENCHMARK_SAMPLES/MASTER_10_DPA_COMPARATIVE_SCORECARD.xlsx")
    if os.path.exists(scorecard_path):
        with open(scorecard_path, "rb") as f:
            st.download_button(
                label="📥 Download 10 DPA Comparative Scorecard (Excel .xlsx)",
                data=f.read(),
                file_name="Master_10_DPA_Comparative_Scorecard.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
    st.subheader("The 10 Companies Evaluated")
    vendors_list = [
        {"Company": "Amazon Web Services (AWS)", "Archetype": "Hyperscale Cloud (IaaS)", "Subprocessor Notice": "30 Days (RSS)", "Breach SLA": "Undue delay", "AI Model Training": "Isolated Bedrock"},
        {"Company": "Microsoft Corporation", "Archetype": "Enterprise Cloud & M365", "Subprocessor Notice": "14 Days (Website)", "Breach SLA": "Aiming for 72h", "AI Model Training": "Commercial Copilot"},
        {"Company": "Google Cloud (GCP)", "Archetype": "Cloud & Workspace", "Subprocessor Notice": "30 Days (Email)", "Breach SLA": "Undue delay", "AI Model Training": "Vertex AI Isolated"},
        {"Company": "Salesforce", "Archetype": "Enterprise CRM SaaS", "Subprocessor Notice": "30 Days (Website)", "Breach SLA": "Aiming for 72h", "AI Model Training": "Einstein Trust Layer"},
        {"Company": "Atlassian", "Archetype": "Collaborative SaaS", "Subprocessor Notice": "30 Days (RSS)", "Breach SLA": "Undue delay", "AI Model Training": "Zero-retention LLMs"},
        {"Company": "Stripe", "Archetype": "Fintech & Payments", "Subprocessor Notice": "30 Days (Dashboard)", "Breach SLA": "Where feasible 48h", "AI Model Training": "Radar Fraud Models"},
        {"Company": "HubSpot", "Archetype": "Marketing Automation", "Subprocessor Notice": "30 Days (Directory)", "Breach SLA": "Within 48 Hours", "AI Model Training": "Tenant Isolation"},
        {"Company": "Cloudflare", "Archetype": "Edge CDN & Security", "Subprocessor Notice": "30 Days (RSS)", "Breach SLA": "Undue delay", "AI Model Training": "Threat Telemetry"},
        {"Company": "Freshworks", "Archetype": "Indian Global SaaS", "Subprocessor Notice": "30 Days (RSS)", "Breach SLA": "Targeting 48 Hours", "AI Model Training": "Tenant Isolated Freddy"},
        {"Company": "Zoho Corporation", "Archetype": "Privacy-First Cloud", "Subprocessor Notice": "30 Days (Portal)", "Breach SLA": "Within 48 Hours", "AI Model Training": "Zero Shared Training"}
    ]
    st.dataframe(pd.DataFrame(vendors_list), width="stretch", hide_index=True)
    
    st.markdown("---")
    st.subheader("Unabridged Legal Specimens")
    c_s1, c_s2 = st.columns(2)
    with c_s1:
        st.markdown("#### 📜 Full 20-Page Enterprise DPA Specimen")
        dpa_spec = load_md_file(r"08_REAL_WORLD_DPA_BENCHMARK_SAMPLES/FULL_UNABRIDGED_ENTERPRISE_DPA_SPECIMEN.md")
        with st.expander("Read Verbatim Master Contract"):
            st.markdown(dpa_spec)
    with c_s2:
        st.markdown("#### 🇪🇺 Official EU SCCs (Module 2)")
        scc_spec = load_md_file(r"08_REAL_WORLD_DPA_BENCHMARK_SAMPLES/EU_COMMISSION_SCCS_2021_914_MODULE_2_FULL.md")
        with st.expander("Read Verbatim European Commission Clauses"):
            st.markdown(scc_spec)

# ----------------------------------------------------
# 9. MODULE 08: GLOBAL PRIVACY POLICY & AUDIT
# ----------------------------------------------------
elif nav_choice == "📜 08. Enterprise Privacy Policy Governance":
    st.header("📜 Module 08: Enterprise Privacy Policy Governance")
    st.caption("Public Notice Compliance under GDPR Arts. 13/14, DPDPA 2023 Sec. 5, and CCPA § 1798.130")
    
    tab_pol, tab_check, tab_how = st.tabs(["🌐 Full Public Privacy Policy Specimen", "📋 25-Point Audit Checklist", "🛠️ How to Draft Policy from RoPA"])
    
    with tab_pol:
        policy_md = load_md_file(r"09_PRIVACY_POLICIES_AND_TRANSPARENCY_GOVERNANCE/FULL_GLOBAL_PRIVACY_POLICY_MASTER_SPECIMEN.md")
        st.markdown(policy_md)
        
    with tab_check:
        check_md = load_md_file(r"09_PRIVACY_POLICIES_AND_TRANSPARENCY_GOVERNANCE/PRIVACY_POLICY_AUDIT_CHECKLIST.md")
        st.markdown(check_md)
        
    with tab_how:
        how_md = load_md_file(r"09_PRIVACY_POLICIES_AND_TRANSPARENCY_GOVERNANCE/HOW_TO_DRAFT_A_PRIVACY_POLICY_FROM_ROPA.md")
        st.markdown(how_md)
