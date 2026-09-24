# 🛡️ FOLDER 06: Step 6 - Data Protection Impact Assessment (DPIA)

### What is in this folder?
- `DPIA_SCREENING_NOTE.md`: The statutory DPIA threshold evaluation.

### Plain English Explanation:
- **What is a DPIA?** Under GDPR Article 35, when a company uses risky or intrusive technology (like recording screens or tracking people across devices), it must perform a formal risk assessment.
- **Why did Miro trigger it?** The European Data Protection Board (EDPB) has 9 risk criteria; meeting 2 makes a DPIA mandatory. Miro met **4 criteria**:
  1. Systematic monitoring (Microsoft Clarity & Hotjar recording mouse movements and screens).
  2. Profiling (Tapad cross-device syncing).
  3. Combining external datasets (LinkedIn & Tapad 3-way cookie syncing).
  4. Large-scale web audience.
- **Critical Violation Found:** Clarity and Hotjar were recording users BEFORE they clicked "Accept All" (Pre-Consent firing).
