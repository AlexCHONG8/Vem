# Summed Medtech DHF Document List with Design Phases

## Summed Project Code System

### Project Code Format
**Format**: `SM[XXX]-[YYY]`

- **SM**: Summed Medtech prefix (required for all projects)
- **XXX**: Project series number (e.g., 100)
- **YYY**: Project model number (e.g., 005 for Adult, 006 for Pediatric)

**Examples**:
- `SM100-005` - Lisa Adult Auto-Injector model
- `SM100-006` - Lucy Pediatric Auto-Injector model
- `SM100-007` - Future product model

### Document Number Format
**Format**: `[XXX]-[YYY]-[DOC_TYPE]-[SEQ]`

- **XXX**: Project series number (3 digits, e.g., 100)
- **YYY**: Project model number (3 digits, e.g., 005, 006)
- **DOC_TYPE**: 3-letter document type code (e.g., URS, DIR, RMP, FTP, STP, RTP, IFU)
- **SEQ**: Sequence number (3 digits, e.g., 001, 002, 003)

**Examples**:
- `100-005-URS-001` - User Requirement Specification for SM100-005, version 001
- `100-006-URS-001` - User Requirement Specification for SM100-006, version 001
- `100-005-RTP-001` - Reliability Test Protocol for SM100-005, sequence 001
- `100-005-STP-002` - Stability Test Plan for SM100-005, sequence 002
- `100-006-IFU-001` - Instructions for Use for SM100-006, version 001

### Document Type Codes (3-Letter System)

| Code | Document Type | Phase | Example Document No. |
|------|---------------|-------|---------------------|
| URS | User Requirement Specification | 1 | 100-005-URS-001 |
| DIR | Design Input Requirements | 2 | 100-005-DIR-001 |
| PRS | Product Requirement Specification | 2 | 100-005-PRS-001 |
| RMP | Risk Management Plan | 2 | 100-005-RMP-001 |
| DFA | Design Failure Mode Analysis | 2 | 100-005-DFA-001 |
| BEP | Biological Evaluation Plan | 2 | 100-000-BEP-001 |
| SIP | Standard Inspection Procedure | 2 | 100-005-SIP-001 |
| BOM | Bill of Materials | 2 | 100-005-BOM-001 |
| IFU | Instructions for Use | 3 | 100-005-IFU-001 |
| FTP | Functional Test Plan | 4 | 100-005-FTP-001 |
| RTP | Reliability Test Protocol | 4 | 100-005-RTP-001 |
| STP | Stability Test Plan | 4 | 100-005-STP-001 |
| DVP | Design Verification Plan | 4 | 100-005-DVP-001 |
| VMP | Validation Master Plan | 4 | 100-005-VMP-001 |
| PSC | Product Specification Confirmation | 4 | 100-005-PSC-001 |
| GSPR | General Safety & Performance Requirements | 1 | 100-005-GSPR-001 |
| MRR | Material Reference Record | 2 | 000-000-MRR-001 |
| PLVP | Product Lifecycle Validation Plan | 4 | 100-005-PLVP-001 |

**Note**: Some documents use `000-000` prefix for company-wide standards (e.g., Biological Evaluation Plan).

---

## DHF Document Master List

**Legend**:
- **Phase**: Design review phase (1-5) for document categorization
- **Short Form**: 3-letter document type code (used in document numbering)
- **QF Code**: Internal Quality Form code (if applicable)
- **Document Number**: Full document number following Summed format
- **Summed Medtech DHF Document Name**: Official English professional name (USE THIS for conversion)

| Phase | Short Form | QF Code | Document Number Example | Chinese Name | Summed Medtech DHF Document Name Standard |
|:-----:|:-----------|:--------|:------------------------|:-------------|:------------------------------------------|
| 1 | PKR | | 100-005-PKR-001 | 产品知识研究 | Product Knowledge Research |
| 1 | CPE | | 100-005-CPE-001 | 竞争对手评估 | Competitive Evaluation |
| 1 | MPR | | 100-005-MPR-001 | 市场价格研究 | Market Price Research |
| 1 | MSC | | 100-005-MSC-001 | 市场样品收集 | Market Sample Collection |
| 1 | BGT | | 100-005-BGT-001 | 费用预算 | Cost Budget |
| 1 | NPA | QF-PM01-01 | 100-005-NPA-001 | 立项申请表 | New Project Application Form |
| 1 | NPR | QF-PM01-02 | 100-005-NPR-001 | 立项书 | New Project Request (NPR) / Project Charter |
| 1 | URS | QF-RD11-01 | 100-005-URS-001 | 客户需求规格 | User Requirement Specification (URS) |
| 1 | IRR | | 100-005-IRR-001 | 产品国际法规 | International Standard and Regulatory Requirements |
| 1 | FTO | | 100-005-FTO-001 | 专利制作自由实施（FTO)声明 | Freedom to Operate (FTO) Statement |
| 1 | GSPR | | 100-005-GSPR-001 | 一般安全和性能要求列表 | General Safety and Performance Requirements (GSPR) Checklist |
| 1 | DR1 | | 100-005-DR1-001 | 产品评估审查会议 | Design Review Meeting Minutes (Phase 1) |
| 1 | DDP | QF-RD11-04 | 100-005-DDP-001 | 设计开发计划书 | Design and Development Plan |
| 2 | DIR | QF-RD11-02 | 100-005-DIR-001 | 设计输入需求 | Design Input Requirements (DIR) |
| 2 | TFA | QF-RD11-07 | 100-005-TFA-001 | 技术可行性分析报告 | Technical Feasibility Analysis Report |
| 2 | MOD | | 100-005-MOD-001 | 模型设计 | 3D Model Design Files |
| 2 | MDC | QF-RD11-54 | 100-005-MDC-001 | 3D模型制作确认清单 | 3D Model Confirmation Checklist |
| 2 | MDV | QF-RD11-31 | 100-005-MDV-001 | 模型验证报告 | Model Verification Report |
| 2 | RMP | | 100-005-RMP-001 | 风险管理计划 (风险性评估) | Risk Management Plan |
| 2 | DFA | QF-RD11-20 | 100-005-DFA-001 | 失效模式分析 | Design Failure Mode and Effects Analysis (DFMEA) |
| 2 | QUO | | 100-005-QUO-001 | 模治具估价 | Mold and Fixture Quotation |
| 2 | DWA | | 100-005-DWA-001 | 2D工程图(组件) | 2D Engineering Drawings (Assembly) |
| 2 | PKG | | 100-005-PKG-001 | 包装设计 | Packaging Design Specifications |
| 2 | PRS | QF-RD11-03 | 100-005-PRS-001 | 设计需求规格书PRS | Product Requirement Specification (PRS) |
| 2 | MRR | QF-RD11-47 | 000-000-MRR-XXX | 材质确认报告 | Material Reference Record (MSDS, RoHS, REACH) |
| 2 | BEP | | 000-000-BEP-001 | 生物学评价计划 及评估报告 | Biological Evaluation Plan and Report (ISO 10993-1) |
| 2 | DR2 | | 100-005-DR2-001 | 设计输入审查会议 | Design Review Meeting Minutes (Phase 2) |
| 2 | DWC | | 100-005-DWC-001 | 2D工程图(零件) | 2D Engineering Drawings (Components) |
| 2 | TFD | | 100-005-TFD-001 | 模治具开发 | Tooling and Fixture Development Records |
| 2 | TDW | | 100-005-TDW-001 | 模具图确认 2D & 3D | Tooling Drawing Confirmation (2D & 3D) |
| 2 | TLS | | 100-005-TLS-001 | 零件加工表 | Tooling List |
| 2 | BOM | QF-RD11-05 | 100-005-BOM-001 | BOM | Bill of Materials (BOM) |
| 2 | SIC | QF-RD11-15 | 100-005-SIC-001 | 零件 SIP | Standard Inspection Procedure (SIP) - Components |
| 2 | SIA | QF-RD11-15 | 100-005-SIA-001 | 组件 SIP | Standard Inspection Procedure (SIP) - Assembly |
| 2 | TR1 | QF-RD11-35 | 100-005-TR1-001 | 试模检讨报告 | T1 Trial Shot Report |
| 2 | TR2 | QF-RD11-35 | 100-005-TR2-001 | 试模检讨报告 | T2 Trial Shot Report |
| 3 | TR3 | | 100-005-TR3-001 | T3 模具验证 (模具厂) | Tooling Validation Report (T3) |
| 3 | DWX | | 100-005-DWX-001 | 2D零件图修正 / SIP 修正 | 2D Component Drawing / SIP Correction Records |
| 3 | FAI | QF-RD11-50/51 | 100-005-FAI-001 | 首件检验（FAI）计划 &报告 | First Article Inspection (FAI) Plan & Report |
| 3 | ESA | | 100-005-ESA-001 | 电气安规测试需求评估 | Electrical Safety Testing Needs Assessment |
| 3 | SVA | | 100-005-SVA-001 | 软件确认评估 | Software Validation Assessment |
| 3 | TVR | | 100-005-TVR-001 | 模具验证 | Tooling Verification Report |
| 3 | MDG | | 100-005-MDG-001 | 模具图修改 | Mold Drawing Modification Records |
| 3 | IFU | QF-RD11-43 | 100-005-IFU-001 | 说明书 | Instructions for Use (IFU) |
| 3 | LBL | | 100-005-LBL-001 | 标签 | Labeling / Artwork |
| 3 | DR3 | | 100-005-DR3-001 | 设计审查会议 | Design Review Meeting Minutes (Phase 3) |
| 3 | SOP | QF-RD11-49 | 100-005-SOP-001 | 组装作业指导书制作 | Assembly Work Instructions (SOP) |
| 3 | PFC | QF-RD11-48 | 100-005-PFC-001 | 制造流程图 | Production Flowchart |
| 3 | QCF | | 100-005-QCF-001 | QC工程图 | Quality Control (QC) Flowchart |
| 3 | EPE | | 100-005-EPE-001 | 生产设备评估 | Production Equipment Evaluation |
| 3 | ETR | QF-RD11-12 | 100-005-ETR-001 | 工程试作 | Engineering Trial Run Report |
| 3 | PIL | | 100-005-PIL-001 | 批量试产 | Pilot Run Report |
| 3 | TIN | QF-RD11-55 | 100-005-TIN-001 | 测试指导 | Testing Instructions |
| 3 | TMV | | 100-005-TMV-001 | 测试方法验证 | Test Method Validation (TMV) Report |
| 3 | PFM | | 100-005-PFM-001 | 制程失效模式分析 | Process Failure Mode and Effects Analysis (PFMEA) |
| 3 | PVR | | 100-005-PVR-001 | 制程验证 | Process Validation Report |
| 3 | MFG | | 100-005-MFG-001 | 制造确认报告 | Manufacturing Confirmation / Trial Production Review |
| 3 | AFV | | 100-005-AFV-001 | 组装/功能验证 | Assembly / Functional Verification Report |
| 3 | RAC | | 100-005-RAC-001 | 风险分析报告确认 | Risk Analysis Report Confirmation |
| 4 | DVM | QF-RD11-14 | 100-005-DVM-001 | 设计验证主矩阵 | Design Verification Master Matrix |
| 4 | VVE | QF-RD11-56 | 100-005-VVE-001 | V&V Test Executive Summary | V&V Test Executive Summary |
| 4 | VMP | QF-RD11-57 | 100-005-VMP-001 | Product V&V Master Plan | Product V&V Master Plan |
| 4 | ASR | QF-RD11-46 | 100-005-ASR-001 | 承認樣品 | Approved Sample Record |
| 4 | UEA | QF-RD11-30 | 100-005-UEA-001 | 可用性工程评估 | Usability Engineering Assessment (IEC 62366) |
| 4 | PSC | | 100-005-PSC-001 | 产品规格确认 | Product Specification Confirmation |
| 4 | DR4 | | 100-005-DR4-001 | 设计验证审查会议 | Design Verification Review Meeting Minutes (Phase 4) |
| 4 | STV | | 100-005-STV-001 | 灭菌确效确认 | Sterilization Validation Report |
| 4 | ESR | | 100-005-ESR-001 | 电气安规测试确认 | Electrical Safety Test Report |
| 4 | CER | | 100-005-CER-001 | 临床评估/临床试验 | Clinical Evaluation Report (CER) |
| 4 | PTV | | 100-005-PTV-001 | 包装/运输验证 | Packaging and Transportation Verification Report |
| 4 | REL | | 100-005-REL-001 | 可靠度测试报告 | Reliability Test Report |
| 4 | STB | | 100-005-STB-001 | 稳定性验证 | Stability Test Report |
| 4 | RET | | 100-005-RET-001 | 加速老化测试 & 时实老化 | Accelerated & Real-Time Aging Test Reports |
| 4 | BER | | 000-000-BER-001 | 生物相容性评价报告 | Biocompatibility Evaluation Report (BER) |
| 4 | UFM | | 100-005-UFM-001 | 使用者失效模式分析 | Use Failure Mode and Effects Analysis (UFMEA) |
| 5 | DR5 | | 100-005-DR5-001 | 设计确认审查会议 | Design Validation Review Meeting Minutes (Phase 5) |
| 5 | DMT | | 100-005-DMT-001 | 技术文件 | Device Master Record (DMR) Technical Documents |
| 5 | DHF | QF-RD11-26 | 100-005-DHF-001 | 设计历史檔案 | Design History File (DHF) Review Checklist |
| 5 | DMR | QF-RD11-27 | 100-005-DMR-001 | DMR 医疗器材主要记录列表审查表 | Device Master Record (DMR) Index / Review Form |
| 5 | PLA | | 100-005-PLA-001 | 产品准证申请 | Product License Application |
| 5 | CAT | | 100-005-CAT-001 | 目录与文宣品 | Catalogs and Brochures |
| 5 | PMS | | 100-005-PMS-001 | 上市后服务确认 | Post-Marketing Service Plan |
| 5 | WBP | | 100-005-WBP-001 | 网站发表 | Website Publication Record |
| 5 | CLS | | 100-005-CLS-001 | 结案(设计审查会议) | Project Closing Review Meeting Minutes |

---

## Design Phase Overview

### Phase 1: Project Initiation & Requirements
**Documents**: PKR, CPE, MPR, MSC, BGT, NPA, NPR, URS, IRR, FTO, GSPR, DR1, DDP
**Focus**: Market research, project approval, user requirements, regulatory requirements

**Key Documents**:
- **URS** (User Requirement Specification): Defines customer needs and product requirements
- **GSPR** (General Safety and Performance Requirements): Regulatory compliance checklist
- **NPR** (New Project Request): Project charter and approval document

### Phase 2: Design Input & Feasibility
**Documents**: DIR, TFA, MOD, MDC, MDV, RMP, DFA, QUO, DWA, PKG, PRS, MRR, BEP, DR2, DWC, TFD, TDW, TLS, BOM, SIC, SIA, TR1, TR2
**Focus**: Design inputs, technical feasibility, risk analysis, tooling development

**Key Documents**:
- **DIR** (Design Input Requirements): Technical specifications and design constraints
- **PRS** (Product Requirement Specification): Comprehensive product requirements
- **RMP** (Risk Management Plan): Risk analysis and mitigation strategies
- **DFA** (Design Failure Mode Analysis): Design risk assessment
- **BOM** (Bill of Materials): Complete material list with suppliers
- **SIP** (Standard Inspection Procedure): Quality inspection criteria

### Phase 3: Design Output & Process Development
**Documents**: TR3, DWX, FAI, ESA, SVA, TVR, MDG, IFU, LBL, DR3, SOP, PFC, QCF, EPE, ETR, PIL, TIN, TMV, PFM, PVR, MFG, AFV, RAC
**Focus**: Tooling validation, process development, production setup

**Key Documents**:
- **IFU** (Instructions for Use): User manual with safety information
- **SOP** (Assembly Work Instructions): Manufacturing assembly procedures
- **PFC** (Production Flowchart): Manufacturing process flow
- **PFM** (Process Failure Mode Analysis): Manufacturing risk assessment
- **PVR** (Process Validation): Production process validation

### Phase 4: Design Verification
**Documents**: DVM, VVE, VMP, ASR, UEA, PSC, DR4, STV, ESR, CER, PTV, REL, STB, RET, BER, UFM
**Focus**: Verification testing, clinical evaluation, biocompatibility, reliability

**Key Documents**:
- **DVM** (Design Verification Master Matrix): Test plan matrix
- **VMP** (Validation Master Plan): Overall validation strategy
- **FTP** (Functional Test Plan): Product functionality testing
- **RTP** (Reliability Test Protocol): Drop testing, transportation testing
- **STP** (Stability Test Plan): Accelerated and real-time aging studies
- **UFM** (Use Failure Mode Analysis): User error risk assessment
- **BER** (Biocompatibility Evaluation Report): ISO 10993 testing results

### Phase 5: Design Validation & Transfer
**Documents**: DR5, DMT, DHF, DMR, PLA, CAT, PMS, WBP, CLS
**Focus**: Validation, regulatory submission, manufacturing transfer, project close

**Key Documents**:
- **DHF** (Design History File): Complete design documentation package
- **DMR** (Device Master Record): Manufacturing documentation
- **PLA** (Product License Application): Regulatory submission

---

## Document Numbering Examples

### Adult Model (SM100-005 - Lisa)
```
100-005-URS-001  (User Requirement Specification)
100-005-DIR-001  (Design Input Requirements)
100-005-PRS-001  (Product Requirement Specification)
100-005-RMP-001  (Risk Management Plan)
100-005-DFA-001  (Design Failure Mode Analysis)
100-005-BOM-001  (Bill of Materials)
100-005-IFU-001  (Instructions for Use)
100-005-FTP-001  (Functional Test Plan)
100-005-RTP-001  (Reliability Test Protocol - Free Fall)
100-005-RTP-002  (Reliability Test Protocol - Simulated Transport)
100-005-STP-001  (Stability Test Plan - Real-time)
100-005-STP-002  (Stability Test Plan - Accelerated)
100-005-DVP-001  (Design Verification Plan)
100-005-VMP-001  (Validation Master Plan)
```

### Pediatric Model (SM100-006 - Lucy)
```
100-006-URS-001  (User Requirement Specification)
100-006-DIR-001  (Design Input Requirements)
100-006-PRS-001  (Product Requirement Specification)
100-006-RMP-001  (Risk Management Plan)
100-006-DFA-001  (Design Failure Mode Analysis)
100-006-BOM-001  (Bill of Materials)
100-006-IFU-001  (Instructions for Use)
100-006-FTP-001  (Functional Test Plan)
100-006-RTP-001  (Reliability Test Protocol - Free Fall)
100-006-RTP-002  (Reliability Test Protocol - Simulated Transport)
100-006-STP-001  (Stability Test Plan - Real-time)
100-006-STP-002  (Stability Test Plan - Accelerated)
100-006-DVP-001  (Design Verification Plan)
100-006-VMP-001  (Validation Master Plan)
```

### Company-Wide Standards (No Model-Specific Number)
```
000-000-BEP-001  (Biological Evaluation Plan - applies to all products)
000-000-MRR-001  (Material Reference Record - specific material)
000-000-MRR-002  (Material Reference Record - another material)
000-000-BER-001  (Biocompatibility Evaluation Report)
```

---

## File Naming Conventions

### HTML Output Files
**Format**: `SM[XXX]-[YYY]-[DOC_TYPE]-[SEQ] [Document Name].html`

**Examples**:
- `SM100-005-URS-001 User Requirement Specification.html`
- `SM100-006-RTP-001 Free Fall Test Protocol.html`
- `SM100-005-STP-002 Accelerated Aging Stability Plan.html`
- `000-000-BEP-001 Biological Evaluation Plan.html`

### Source Files
**Format**: `[DOC_TYPE]-[SEQ] [Chinese Name].md`

**Examples**:
- `URS-001 客户需求规格.md`
- `RTP-001 可靠性试验方案-自由跌落.md`
- `STP-002 稳定性试验方案-加速老化.md`

---

## Quick Reference: Common Document Types

| Document Type | Short Code | Phase | Adult Example | Pediatric Example |
|---------------|------------|-------|---------------|-------------------|
| User Requirement Specification | URS | 1 | 100-005-URS-001 | 100-006-URS-001 |
| Design Input Requirements | DIR | 2 | 100-005-DIR-001 | 100-006-DIR-001 |
| Risk Management Plan | RMP | 2 | 100-005-RMP-001 | 100-006-RMP-001 |
| Bill of Materials | BOM | 2 | 100-005-BOM-001 | 100-006-BOM-001 |
| Instructions for Use | IFU | 3 | 100-005-IFU-001 | 100-006-IFU-001 |
| Functional Test Plan | FTP | 4 | 100-005-FTP-001 | 100-006-FTP-001 |
| Reliability Test Protocol | RTP | 4 | 100-005-RTP-001 | 100-006-RTP-001 |
| Stability Test Plan | STP | 4 | 100-005-STP-001 | 100-006-STP-001 |
| Design Verification Plan | DVP | 4 | 100-005-DVP-001 | 100-006-DVP-001 |
| Validation Master Plan | VMP | 4 | 100-005-VMP-001 | 100-006-VMP-001 |

---

**Last Updated**: 2026-01-17
**Project**: Summed Medtech DHF Documentation System
**Customer**: Vem Pharma Turkey
