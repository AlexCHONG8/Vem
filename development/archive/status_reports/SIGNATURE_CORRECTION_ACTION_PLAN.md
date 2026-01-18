# Signature Correction Action Plan
**Generated**: 2026-01-14
**Reference**: TEAM_MEMBERS_REFERENCE.md v3.3
**Scope**: All 33 HTML documents requiring signature corrections

---

## 📊 Summary of Issues Identified

### Critical Issues Requiring Correction:

1. **Chinese Names in Signatures** (HIGH PRIORITY)
   - 10 documents contain direct-translated Chinese names
   - Must use correct English names from TEAM_MEMBERS_REFERENCE.md

2. **Incorrect GM Name** (CRITICAL - Just Corrected)
   - Andy Tsai → **Tony Tsai** (GM001)
   - Affects all documents with GM001 signature

3. **Resigned Personnel Signatures** (MEDIUM PRIORITY)
   - 15 documents contain signatures from resigned team members
   - Historical signatures may be preserved for audit trail

4. **Format Inconsistencies** (LOW PRIORITY)
   - 26 documents use vertical format instead of horizontal
   - Standardization required for consistency

---

## 🎯 Action Plan by Priority

### Phase 1: CRITICAL Name Corrections (1-2 days)

#### 1.1 Update Tony Tsai Name (GM001) - ALL DOCUMENTS
**Affected**: All documents with "Andy Tsai" as approver

**Required Changes**:
```
Andy Tsai → Tony Tsai
```

**Documents to Update** (from SIGNATURE_STATUS_REPORT.md):
- 100-005-RMP-001_Risk_Management_Plan.html
- 100-005-RAC-001_Risk_Analysis_Report_Confirmation.html
- 100-005-DFA-001_Design_Failure_Mode_Effects_Analysis.html
- 100-005-DMR-001_DMR_Index_Review_Form.html
- 100-005-LBL-001_Labeling_Artwork.html
- 100-005-IFU-001_Instructions_for_Use.html
- 100-005-CER-001_Clinical_Evaluation_Report.html
- Plus any other documents with GM001 approval

#### 1.2 Fix Chinese Name Translations (10 documents)

**Correct Name Mappings**:
| Current (WRONG) | Correct (ENGLISH) | Documents Affected |
|----------------|-------------------|-------------------|
| Rongren Yang | **Zen Yang** (QM001) | PFA-001, RMP-001 |
| Zhangyun Gao | **ZY Gao** (PD002) | PFA-001, SIP documents |
| Yanghua Su | **YH Su** (Active) | PFA-001, SIP documents |
| Chenjun Weng | **Nic Weng** (RD005) | DFA-001 |
| Dianjia Zhao | **Logan Zhao** (RD002) | DFA-001 |
| Pengtao Gao | **Alvin Gao** (RD003) | DFA-001 |

**Specific File Updates**:

**01-risk-management/100-000-PFA-001_Process_Failure_Mode_Effects_Analysis.html**:
```html
<!-- BEFORE -->
<div class="signature-name">/s/ Yanghua Su</div>
<div class="signature-name">/s/ Zhangyun Gao</div>
<div class="signature-name">/s/ Rongren Yang</div>

<!-- AFTER -->
<div class="signature-name">/s/ YH Su</div>
<div class="signature-name">/s/ ZY Gao</div>
<div class="signature-name">/s/ Zen Yang</div>
```

**01-risk-management/100-005-DFA-001_Design_Failure_Mode_Effects_Analysis.html**:
```html
<!-- BEFORE -->
<div class="signature-name">/s/ Chenjun Weng</div>
<div class="signature-name">/s/ Dianjia Zhao</div>
<div class="signature-name">/s/ Pengtao Gao</div>

<!-- AFTER -->
<div class="signature-name">/s/ Nic Weng</div>
<div class="signature-name">/s/ Logan Zhao</div>
<div class="signature-name">/s/ Alvin Gao</div>
```

**01-risk-management/100-005-RMP-001_Risk_Management_Plan.html**:
```html
<!-- BEFORE -->
<div class="signature-name">/s/ Rongren Yang</div>

<!-- AFTER -->
<div class="signature-name">/s/ Zen Yang</div>
```

**SIP Documents** (100-005-SIP-001/011/012/014/015/016/017/018):
- All in `04-design-output/` folder
- Replace `Yanghua Su` → `YH Su`
- Replace `Zhangyun Gao` → `ZY Gao`

#### 1.3 Fix Typo: YC Yang → YC Zheng

**File**: 03-design-verification/100-005-FTP-001_Functional_Test_Plan.html
```html
<!-- BEFORE -->
<div class="signature-name">/s/ YC Yang</div>

<!-- AFTER -->
<div class="signature-name">/s/ YC Zheng</div>
```

---

### Phase 2: Resigned Personnel Assessment (2-3 days)

**IMPORTANT NOTE**: User confirmed: "do not remove the resigned personal since sinagture history still need to keep"

**Decision Required**: For each resigned personnel signature, determine:
- ✅ **KEEP** if: Historical audit trail, document revision not required
- 🔄 **UPDATE** if: Document requires current revision
- 📝 **ANNOTATE** if: Add note about resignation date

#### 2.1 Resigned Personnel Found

| Name | ID | Resignation Date | Documents Affected | Action |
|------|----|----|----|----|
| **Coco Xu** | RD004 | 2025-10-31 | 4 MRR documents | Assess per document |
| **ZZ Huang** | RD006 | 2025-01-31 | PRS-001 | Keep (historical) |
| **Nic Weng** | RD005 | 2025-08-31 | DFA-001 | Keep (historical) |
| **Alvin Gao** | RD003 | 2025-10-01 | DFA-001 | Keep (historical) |
| **Jimmy Xu** | PE001 | 2025-09-30 | BEP-001, 4 MRR docs | Assess per document |
| **Kayla Li** | QE001 | 2024-09-30 | RMP-001, RAC-001 | Keep (historical) |
| **ZY Gao** | PD002 | 2025-04-30 | PFA-001, 8 SIP docs | Keep (historical) |

**Recommendation**: Keep all historical signatures as-is for audit trail. Only update when document revisions are officially required.

---

### Phase 3: Format Standardization (3-4 days)

**Required**: Convert 26 documents from vertical to horizontal signature format

**Standard Format**:
```html
<table class="signature-table">
    <tr>
        <td>
            <div class="signature-block">
                <div class="signature-name">Timi Xiong</div>
                <div class="signature-title">RD Engineer</div>
                <div class="signature-line"></div>
                <div class="signature-label">Prepared by</div>
            </div>
        </td>
        <td>
            <div class="signature-block">
                <div class="signature-name">Zen Yang</div>
                <div class="signature-title">ISO13485 Management Representative</div>
                <div class="signature-line"></div>
                <div class="signature-label">Reviewed by</div>
            </div>
        </td>
        <td>
            <div class="signature-block">
                <div class="signature-name">Kevin Lo</div>
                <div class="signature-title">RD Director</div>
                <div class="signature-line"></div>
                <div class="signature-label">Approved by</div>
            </div>
        </td>
    </tr>
</table>
```

**Files Needing Format Conversion**:
- Most documents with `<thead>` in signature tables
- Convert to single `<tr>` with 3 `<td>` elements
- Ensure equal column widths (33.33%)

---

## 📋 Detailed File-by-File Correction List

### Priority 1: CRITICAL (Tony Tsai + Chinese Names)

#### 01-risk-management/ (6 files)
1. **100-000-PFA-001** - Chinese names (Yanghua Su→YH Su, Zhangyun Gao→ZY Gao, Rongren Yang→Zen Yang)
2. **100-005-DFA-001** - Chinese names (Chenjun Weng→Nic Weng, Dianjia Zhao→Logan Zhao, Pengtao Gao→Alvin Gao) + Tony Tsai
3. **100-005-RMP-001** - Chinese name (Rongren Yang→Zen Yang) + Tony Tsai
4. **100-005-RAC-001** - Tony Tsai + resigned Kayla Li (keep historical)
5. **100-005-SPR-001** - ✅ Already correct
6. **100-005-UFM-001** - Format issue + resigned personnel

#### 02-design-input/ (6 files)
1. **100-005-URS-001** - ✅ Correct
2. **100-005-PRS-001** - Resigned ZZ Huang, Nic Weng (keep historical)
3. **100-005-MAT-001** - ✅ Correct
4. **100-005-PSC-001** - ✅ Correct
5. **100-005-DIR-001** - ✅ Correct
6. **100-005-VVE-001** - ✅ Correct

#### 03-design-verification/ (5 files)
1. **100-000-BEP-001** - Chinese names + resigned Jimmy Xu
2. **100-005-CER-001** - Tony Tsai
3. **100-005-DVP-001** - Format issue
4. **100-005-FTP-001** - Typo: YC Yang→YC Zheng
5. **100-005-RTP-001/002/003** - Check for Tony Tsai

#### 04-design-output/ (3+ files)
1. **100-005-DHF-001** - ✅ Correct
2. **100-005-DMR-001** - Tony Tsai
3. **100-005-LBL-001** - Tony Tsai
4. **100-005-SIP-001/011/012/014/015/016/017/018** - Chinese names (Yanghua Su→YH Su, Zhangyun Gao→ZY Gao)

#### 02-design-input/MRR documents/ (4 files)
1. **000-000-MRR-008/011/012/013** - Resigned Coco Xu, Jimmy Xu (assess per document)

---

## 🔍 Verification Checklist

After completing corrections, verify each document:

- [ ] All signature names are 100% English (no Chinese characters)
- [ ] All names match TEAM_MEMBERS_REFERENCE.md v3.3
- [ ] Tony Tsai used instead of Andy Tsai
- [ ] Correct English names (YH Su, ZY Gao, Zen Yang - not Yanghua Su, Zhangyun Gao, Rongren Yang)
- [ ] Historical signatures preserved for audit trail
- [ ] Consistent 3-person horizontal format
- [ ] Correct approval matrix for document type
- [ ] No typos (YC Zheng not YC Yang)

---

## 📝 Implementation Order

### Day 1: Critical Name Corrections
1. Update all Andy Tsai → Tony Tsai (batch operation)
2. Fix Chinese names in PFA-001, DFA-001, RMP-001
3. Fix Chinese names in all 8 SIP documents
4. Fix YC Yang → YC Zheng typo in FTP-001

### Day 2: Document-by-Document Review
1. Review remaining documents for Chinese names
2. Update Tony Tsai in remaining documents
3. Verify all name corrections against TEAM_MEMBERS_REFERENCE.md v3.3

### Day 3: Resigned Personnel Assessment
1. Document which resigned personnel appear where
2. Make decision: keep historical vs update
3. Apply updates only where document revisions required

### Day 4-5: Format Standardization
1. Convert vertical to horizontal format
2. Standardize signature block styling
3. Final verification of all changes

---

## ✅ Success Criteria

Before Vem Pharma Turkey audit:

1. **100% English Names**: Zero Chinese characters in signatures
2. **Correct Names**: All names match TEAM_MEMBERS_REFERENCE.md v3.3
3. **GM Name**: All documents use Tony Tsai (not Andy Tsai)
4. **Historical Integrity**: Resigned personnel signatures preserved appropriately
5. **Format Consistency**: All signatures use horizontal 3-person format
6. **Audit Trail**: All changes documented with dates and reasons

---

**Next Steps**:
1. ✅ Obtain user approval for this action plan
2. ⏭️ Begin Phase 1: Critical Name Corrections
3. 📋 Track progress with completion checklist
4. 🔄 Update SIGNATURE_STATUS_REPORT.md after corrections

**Reference Documents**:
- TEAM_MEMBERS_REFERENCE.md v3.3
- final_signature_verification_report.md
- SIGNATURE_STATUS_REPORT.md

---

**Plan Prepared**: 2026-01-14
**Status**: Ready for Implementation
**Estimated Completion**: 5-7 business days
