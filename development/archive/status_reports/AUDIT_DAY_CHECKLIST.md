# Vem Pharma Audit - Day-by-Day Checklist

**Audit Dates**: [TBD]
**Auditor**: Vem Pharma Regulatory Team
**Auditee**: Summed Medtech 森迈医疗
**Location**: Jiaxing Summed Medtech Co., Ltd.

---

## Pre-Audit Preparation (1 Day Before)

### ✅ Document Verification
- [ ] Run `fix_index_links.sh` to correct all broken links in index.html
- [ ] Open index.html in browser and test all 29 document links
- [ ] Verify all 4 quick links work (Org Chart, Flowchart, ISO Certificate, Video)
- [ ] Print VEM_AUDIT_LINK_STATUS_REPORT.md for reference
- [ ] Prepare physical sample devices (Lisa Adult & Lucy Pediatric models)

### ✅ Room & Equipment Setup
- [ ] Set up conference room with projector/monitor for document review
- [ ] Test video playback: "Summed Anji.mp4" (12MB)
- [ ] Open ISO 13485 certificate PDF: verify it loads correctly
- [ ] Prepare Design History File folder structure display
- [ ] Have backup laptop with all documents loaded

### ✅ Team Briefing
- [ ] Brief all document owners on audit trail questions
- [ ] Prepare availability for:
  - [ ] RD Manager (Logan Zhao) - Design verification questions
  - [ ] QA Manager (Ryzer Zhou) - Risk management questions
  - [ ] ISO13485 MR (Zen Yang) - Quality system questions
  - [ ] RD Engineer (Timi Xiong) - Technical document questions

---

## AUDIT DAY 1 - Design Controls & Risk Management

### **Morning Session: Design Planning & Input** (3 hours)

#### **08:30-09:00: Welcome & Opening**
- [ ] Welcome auditor, provide coffee/tea
- [ ] Present org chart (Summed_Org_Chart.html)
- [ ] Show facility overview video (Summed Anji.mp4)
- [ ] Explain product family (Lisa Adult SM100-005, Lucy Pediatric SM100-006)

#### **09:00-10:00: Design Planning Phase**
- [ ] **DVP-001**: Design V&V Master Plan
  - [ ] Explain overall verification strategy
  - [ ] Show timeline and responsible departments
  - [ ] Highlight links to all test protocols
- [ ] **Simject_Assembly_Flowchart.html**
  - [ ] Walk through manufacturing process flow
  - [ ] Identify quality control checkpoints

#### **10:00-11:30: Design Input Phase** ⭐ CRITICAL SECTION
- [ ] **URS-001**: User Requirement Specification
  - [ ] Section 5: Intended use
  - [ ] Section 6: Target patient population (Adult vs Pediatric)
  - [ ] Section 11: Requirements (all features user needs)
  - [ ] **TRACEABILITY**: Show how URS flows to PRS-001

- [ ] **PRS-001**: Product Requirement Specification
  - [ ] Technical specifications (dose accuracy, activation force)
  - [ ] Performance criteria (all measurable parameters)
  - [ ] Interface requirements (patient-device interaction)
  - [ ] **TRACEABILITY**: Show how PRS requirements verified in FTP-001

- [ ] **PSC-001**: Product Specification Confirmation *(ask if auditor wants to see)*
  - [ ] Design freeze approval
  - [ ] Final specs before verification phase

#### **11:30-12:30: Material & Biocompatibility**
- [ ] **MAT-001**: Material Review Report Summary
  - [ ] Overall material compliance strategy
- [ ] **MRR-008/011/012/013**: Individual Material Reports
  - [ ] MRR-008: Hytrel 6356 (needle shield material)
  - [ ] MRR-011: PC+ABS (housing material)
  - [ ] MRR-012: POM FG500P (internal components)
  - [ ] MRR-013: Polycarbonate (transparent components)
  - [ ] **TRACEABILITY**: Show MRR → BEP-001 link

---

### **Afternoon Session: Risk Management** (3 hours)

#### **14:00-17:00: Risk Analysis** ⭐ CRITICAL SECTION

- [ ] **RMP-001**: Risk Management Plan
  - [ ] Section 2: Risk management process (ISO 14971)
  - [ ] Section 3: Risk acceptability criteria
  - [ ] Section 4: Risk analysis methodology
  - [ ] **KEY POINT**: Explain 3-type FMEA strategy

- [ ] **DFA-001**: Design Failure Mode Effects Analysis
  - [ ] Show top 5 design hazards by risk priority number (RPN)
  - [ ] Explain mitigation design features
  - [ ] **TRACEABILITY**: Show DFA → FTP-001 verification link
  - [ ] Example: "Risk: Needle fails to extend → Design: Redundant spring → Verified in FTP-001 Section 5.2"

- [ ] **PFA-001**: Process Failure Mode Effects Analysis
  - [ ] Show top 5 manufacturing process risks
  - [ ] Explain process controls (SIP inspections)
  - [ ] **TRACEABILITY**: Show PFA → Assembly Flowchart link
  - [ ] Example: "Risk: Incorrect assembly torque → Control: Torque tool validation in SIP-012"

- [ ] **UFM-001**: Use Failure Mode Effects Analysis
  - [ ] Show top 5 use error scenarios
  - [ ] Explain user interface design features
  - [ ] **TRACEABILITY**: Show UFM → IFU-001 warnings link
  - [ ] Example: "Risk: User holds device upside down → Warning in IFU-001 Section 6.3 with illustration"

- [ ] **RAC-001**: Risk Analysis Report Confirmation
  - [ ] Overall risk-benefit conclusion
  - [ ] Summary of all residual risks
  - [ ] Risk management effectiveness review

---

## AUDIT DAY 2 - Verification, Validation & Output

### **Morning Session: Design Verification** (3 hours)

#### **08:30-11:30: Verification Testing** ⭐ CRITICAL SECTION

- [ ] **FTP-001**: Functional Test Plan
  - [ ] Section 4: Test methods overview
  - [ ] Section 5: Activation force test (5-35 N requirement)
  - [ ] Section 6: Dose accuracy test (±10% requirement)
  - [ ] Section 7: Needle extension test (≥0.5in Adult, ≥0.4in Pediatric)
  - [ ] **TRACEABILITY TABLE**:
    - [ ] PRS-001 requirement → FTP-001 test method → Acceptance criterion
    - [ ] DFA-001 hazard → FTP-001 verification test → Result

- [ ] **STP-001**: Real-time Aging Stability Plan
  - [ ] Section 3: Test conditions (25°C/60%RH)
  - [ ] Section 4: Test intervals (0, 3, 6, 9, 12, 18, 24, 36 months)
  - [ ] Section 5: Test parameters (dose accuracy, activation force)
  - [ ] **KEY POINT**: Shelf-life claim support (24 months)

- [ ] **STP-002**: Accelerated Aging Stability Plan
  - [ ] Section 3: Accelerated conditions (40°C/75%RH)
  - [ ] Section 4: Arrhenius equation justification
  - [ ] **KEY POINT**: Real-time aging prediction method

- [ ] **RTP-001**: Free Fall Test Protocol
  - [ ] Section 3: Drop heights (1 meter for packaged device)
  - [ ] Section 4: Test orientations (6 orientations)
  - [ ] Section 5: Post-drop functional testing
  - [ ] **TRACEABILITY**: DFA-001 handling risk → RTP-001 verification

- [ ] **RTP-002**: Simulated Transport Test Protocol
  - [ ] Section 3: Vibration test parameters
  - [ ] Section 4: Truck transport simulation
  - [ ] **KEY POINT**: Distribution validation for shipping claims

#### **11:30-12:30: V&V Summary**
- [ ] **VVE-001**: V&V Test Executive Summary *(ask if auditor wants to see)*
  - [ ] Overall test results summary
  - [ ] Pass/fail status for all verification tests
  - [ ] Design validation conclusion

---

### **Afternoon Session: Clinical, Materials & Transfer** (3 hours)

#### **14:00-15:00: Clinical Evaluation & Biocompatibility**

- [ ] **BEP-001**: Biological Evaluation Plan
  - [ ] Section 2: ISO 10993-1 categorization (surface device, <24h contact)
  - [ ] Section 3: Required testing (cytotoxicity, sensitization, irritation)
  - [ ] **TRACEABILITY**: MRR material data → BEP testing strategy

- [ ] **CER-001**: Clinical Evaluation Report
  - [ ] Section 3: State-of-the-art analysis (epinephrine auto-injectors)
  - [ ] Section 4: Clinical literature review
  - [ ] Section 5: Benefit-risk assessment
  - [ ] **KEY POINT**: Demonstrates equivalence to marketed devices

#### **15:00-17:00: Design Output & Transfer** ⭐ CRITICAL SECTION

- [ ] **BOM-001**: Bill of Materials (Interactive Dashboard)
  - [ ] Show complete component tree structure
  - [ ] Drill into critical components (needle shield, spring, housing)
  - [ ] **TRACEABILITY**: BOM component → MRR material spec → BEP test

- [ ] **SIP-001/011/012/014**: Standard Inspection Procedures
  - [ ] SIP-001: Front Component Inspection (critical dimensions)
  - [ ] SIP-011: Rear Cover Inspection (molded features)
  - [ ] SIP-012: Actuation Rod Inspection (spring interface)
  - [ ] SIP-014: Push Rod Inspection (force transmission)
  - [ ] **TRACEABILITY**: PRS-001 spec → SIP acceptance criterion

- [ ] **DMR-001**: DMR Index Review Form
  - [ ] Complete Device Master Record document list
  - [ ] Show all manufacturing procedures referenced
  - [ ] **KEY POINT**: Design transfer completeness

- [ ] **DHF-001**: DHF Review Checklist
  - [ ] Complete DHF document index
  - [ ] Design control compliance checklist (FDA 21 CFR 820.30)
  - [ ] **KEY POINT**: Audit trail document

---

## AUDIT DAY 3 - Labeling, GSPR & Closing

### **Morning Session: Labeling & Compliance** (2 hours)

#### **08:30-10:30: Labeling & Instructions** ⭐ CRITICAL SECTION

- [ ] **IFU-001**: Instructions for Use (14 sections)
  - [ ] Section 1: Product Introduction
  - [ ] Section 6: **Major Warnings & Contraindications** (UFM-001 traceability)
    - [ ] Show 6 major warnings with illustrations
    - [ ] Explain how UFM-001 use errors addressed in warnings
  - [ ] Section 8: **How to Use** (step-by-step with illustrations)
    - [ ] Show 9-step process
    - [ ] Demonstrate URS-001 user needs addressed
  - [ ] **TRACEABILITY MATRIX**:
    - [ ] URS-001 user need → IFU-001 instruction
    - [ ] UFM-001 use error → IFU-001 warning
    - [ ] PRS-001 feature → IFU-001 description

#### **10:30-11:30: General Safety & Performance Requirements**

- [ ] **SPR-001**: GSPR Checklist (MDR Annex I)
  - [ ] Section 1: General requirements (Annex I Chapter I)
  - [ ] Section 2: Requirements regarding safety & performance (Chapter II)
  - [ ] Section 3: Chemical, physical & biological properties (Chapter III)
  - [ ] **TRACEABILITY**:
    - [ ] CER-001 clinical data → GSPR Chapter I compliance
    - [ ] DFA/PFA/UFM risk analysis → GSPR Chapter II compliance
    - [ ] BEP-001 biocompatibility → GSPR Chapter III compliance
    - [ ] FTP/STP/RTP verification → GSPR Chapter IV compliance

---

### **Late Morning: Certification & Closing** (1 hour)

#### **11:30-12:30: Quality System Certification**

- [ ] **ISO13485 Certificate**: Present PDF certificate
  - [ ] Certificate validity period
  - [ ] Scope of certification (medical device manufacturing)
  - [ ] Certification body accreditation

- [ ] **Audit Corrective Action Report 2024**
  - [ ] Previous audit findings (if any)
  - [ ] Corrective actions taken
  - [ ] Evidence of continuous improvement

#### **12:30-13:00: Closing & Q&A**
- [ ] Auditor summary of findings
- [ ] Request for additional documents (if any)
- [ ] Timeline for audit report delivery
- [ ] Thank auditor, schedule follow-up if needed

---

## Post-Audit Actions

### **Day of Audit (After Auditor Leaves)**
- [ ] Debrief with team: What went well? What needs improvement?
- [ ] Document auditor questions and responses
- [ ] Note any requested additional documents
- [ ] Send thank-you email to auditor

### **Within 1 Week**
- [ ] Address any minor findings (document observations)
- [ ] Provide any requested additional documents
- [ ] Schedule follow-up meeting if needed
- [ ] Update DHF with any new documents generated during audit

### **Within 1 Month**
- [ ] Implement corrective actions for any findings
- [ ] Update risk analysis if new hazards identified
- [ ] Conduct management review of audit results
- [ ] Plan for next audit/surveillance visit

---

## Traceability Cheat Sheet (Quick Reference)

### **Design Input → Verification**
```
URS-001 → PRS-001 → PSC-001
    ↓
DVP-001 (Master Plan)
    ↓
FTP-001 (Functional) ──┐
STP-001/002 (Stability)─┼─→ VVE-001 (Summary)
RTP-001/002 (Transport)─┘
```

### **Risk Management**
```
RMP-001 (Plan)
    ↓
DFA-001 (Design) ──┐
PFA-001 (Process)──┼─→ RAC-001 (Confirmation)
UFM-001 (Use)─────┘
    ↓
SPR-001 (GSPR compliance)
```

### **Materials & Biocompatibility**
```
MRR-008/011/012/013 (Material specs)
    ↓
BEP-001 (Bioeval plan)
    ↓
CER-001 (Clinical eval)
```

### **Design Output**
```
BOM-001 (Components)
    ↓
SIP-001/011/012/014 (Inspection)
    ↓
DMR-001 (Device Master Record)
    ↓
DHF-001 (DHF Checklist)
```

### **Labeling**
```
URS-001 (User needs) ──┐
UFM-001 (Use errors)───┼─→ IFU-001 (Instructions)
PRS-001 (Features)────┘
```

---

## Emergency Contacts During Audit

| Role | Name | Contact | Responsibility |
|------|------|---------|----------------|
| ISO13485 MR | Zen Yang | [phone] | Quality system questions |
| RD Manager | Logan Zhao | [phone] | Design verification |
| QA Manager | Ryzer Zhou | [phone] | Risk management |
| RD Engineer | Timi Xiong | [phone] | Technical documents |
| BD Director | Alex Chong | [phone] | General coordination |

---

**Remember**: The auditor is looking for **traceability** between documents. Always show the link:
- Requirement → Verification → Validation
- Hazard → Mitigation → Verification
- Material → Test → Compliance

**Good luck! 🍀**

---

**End of Checklist**
