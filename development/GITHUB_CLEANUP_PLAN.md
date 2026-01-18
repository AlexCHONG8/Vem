# GitHub Cleanup Plan - Vem Audit Documentation
**Created**: 2026-01-15
**Purpose**: Clean and organize repository structure after 3 days of refinement
**Target**: Clean GitHub upload ready for audit

---

## 📋 Current State Analysis

### Total Files Found
- **HTML documents**: 31 production + 20 backup (.bak) = 51 files
- **Markdown reports**: 15 status/tracking files
- **Python scripts**: 5 temporary analysis scripts
- **Shell scripts**: 2 temporary fix scripts
- **Backup directories**: 1 (backup_2026-01-14_pre-reorg/)
- **Root clutter**: 20+ loose files

### Problems Identified
1. ❌ **20+ .bak files** scattered across documents/
2. ❌ **15 status reports** cluttering root directory
3. ❌ **5 Python scripts** used for signature analysis (no longer needed)
4. ❌ **Multiple README files** (README.md, README_AUDIT_SUMMARY.md)
5. ❌ **Two index files** (index.html, index_refined.html) - need to choose one
6. ❌ **Backup directory** taking up space
7. ❌ **Agent/Claude temp directories** (.agent/, .claude/)
8. ❌ **Example HTML files** (signature-*.html) - development artifacts

---

## 🎯 Cleanup Strategy

### Phase 1: Create Archive (Keep for Safety)

```bash
# Create archive directory for all temporary files
mkdir -p archive/work_2026-01-12_to_2026-01-15
mkdir -p archive/status_reports
mkdir -p archive/development_artifacts
mkdir -p archive/backup_files
```

### Phase 2: File Actions

#### 2.1 Files to DELETE (20+ backup files)

**All .bak files in documents/**:
```bash
# Design Input backups
documents/02-design-input/100-005-PRS-001_Product_Requirement_Specification.html.bak
documents/02-design-input/100-005-URS-001_User_Requirement_Specification.html.bak

# Design Verification backups
documents/03-design-verification/100-000-BEP-001_Biological_Evaluation_Plan.html.bak
documents/03-design-verification/100-005-FTP-001_Functional_Test_Plan.html.bak
documents/03-design-verification/100-005-RTP-001_Free_Fall_Test_Protocol.html.bak
documents/03-design-verification/100-005-RTP-002_Simulated_Transport_Test_Protocol.html.bak
documents/03-design-verification/100-005-STP-001_Real-time_Aging_Stability_Plan.html.bak
documents/03-design-verification/100-005-STP-002_Accelerated_Aging_Stability_Plan.html.bak

# Design Output backups
documents/04-design-output/100-005-IFU-001_Instructions_for_Use.html.bak

# Materials backups
documents/07-materials-components/100-005-SIP-001_Front_Component_Inspection_Specification.html.bak
documents/07-materials-components/100-005-SIP-011_Rear_Cover_Inspection_Specification.html.bak
documents/07-materials-components/100-005-SIP-012_Actuation_Rod_Inspection_Specification.html.bak
documents/07-materials-components/100-005-SIP-014_Push_Rod_Inspection_Specification.html.bak

# Risk Management backups
documents/01-risk-management/100-005-RAC-001_Risk_Analysis_Report_Confirmation.html.bak
documents/01-risk-management/100-005-RMP-001_Risk_Management_Plan.html.bak

# BOM backups
documents/100-005-BOM-001_Dashboard.html.bak
documents/100-005-BOM-001_Dashboard.html.bak3
documents/100-005-BOM-001_Dashboard.html.bak4

# Reference backups
reference/TEAM_MEMBERS_REFERENCE.md.backup
```

**Action**: Move all .bak files to `archive/backup_files/`

#### 2.2 Files to ARCHIVE (Status Reports - 15 files)

```bash
# Move all status/tracking reports to archive/status_reports/
AUDIT_DAY_CHECKLIST.md
SIGNATURE_STATUS_REPORT.md
SIGNATURE_CORRECTION_ACTION_PLAN.md
SIGNATURE_UPDATES_COMPLETED.md
PATH_FIXES_COMPLETE.md
FOLDER_REORGANIZATION_COMPLETE.md
GSPR_FINAL_VERIFICATION.md
VEM_AUDIT_LINK_STATUS_REPORT.md
final_signature_verification_report.md
README_AUDIT_SUMMARY.md (consolidate into main README.md)
```

**Action**: Move to `archive/status_reports/`

#### 2.3 Files to ARCHIVE (Development Scripts - 7 files)

```bash
# Python scripts (signature analysis)
analyze_signatures.py
analyze_signatures_fixed.py
detailed_signature_analysis.py

# Shell scripts
final_summary.sh
fix_index_links.sh

# Example HTML files (development artifacts)
signature-dashboard-example.html
signature-example-enhanced.html

# Excel conversion script
Excel/convert_bom_csv_to_html.py
```

**Action**: Move to `archive/development_artifacts/`

#### 2.4 Files to ARCHIVE (Temporary Directories)

```bash
# Agent/Claude working directories
.agent/
.claude/

# Source markdown (Chinese originals - keep for reference)
Vem audit doc markdown/ → archive/sources/

# Backup directory
backup_2026-01-14_pre-reorg/ → archive/
```

#### 2.5 Files to CONSOLIDATE

**README Files**:
- Keep: `README.md` (main documentation)
- Archive: `README_AUDIT_SUMMARY.md` (content merged into README.md)

**Index Files**:
- **Decision Required**: Choose `index_refined.html` for audit structure
- Archive: `index.html` (or vice versa)

---

## 📁 Final Directory Structure (After Cleanup)

```
Vem audit/
├── .git/
├── .gitignore
├── CLAUDE.md                          # Project guide for Claude
├── README.md                          # Main project README
│
├── index.html                         # Main navigation index (CHOOSE: index_refined.html)
├── Summed_Org_Chart.html              # Organization chart
├── Simject_Assembly_Flowchart.html    # Assembly flowchart
│
├── assets/                            # Static assets
│   ├── css/
│   │   └── summed-medtech-docs.css
│   └── images/
│       ├── Summed logo.png
│       ├── 100-005-IFU-*.png
│       ├── 100-005-RMP-*.png
│       ├── 100-005-SPR-*.jpg
│       ├── ISO13485 EN.pdf
│       └── Summed Anji.mp4
│
├── documents/                         # ✅ PRODUCTION DOCUMENTS (31 files, NO .bak)
│   ├── 01-risk-management/           # 6 documents
│   │   ├── 100-000-PFA-001_Process_Failure_Mode_Effects_Analysis.html
│   │   ├── 100-005-DFA-001_Design_Failure_Mode_Effects_Analysis.html
│   │   ├── 100-005-RMP-001_Risk_Management_Plan.html
│   │   ├── 100-005-UFM-001_Use_Failure_Mode_Effects_Analysis.html
│   │   ├── 100-005-RAC-001_Risk_Analysis_Report_Confirmation.html
│   │   └── 100-005-SPR-001_General_Safety_and_Performance_Requirements_CHECKLIST.html
│   │
│   ├── 02-design-input/              # 4 documents
│   │   ├── 100-005-URS-001_User_Requirement_Specification.html
│   │   ├── 100-005-PRS-001_Product_Requirement_Specification.html
│   │   ├── 100-005-PSC-001_Product_Specification_Confirmation.html
│   │   └── 100-005-MAT-001_Material_Review_Report.html
│   │
│   ├── 03-design-verification/       # 9 documents
│   │   ├── 100-000-BEP-001_Biological_Evaluation_Plan.html
│   │   ├── 100-005-DVP-001_Design_Verification_and_Validation_Master_Plan.html
│   │   ├── 100-005-FTP-001_Functional_Test_Plan.html
│   │   ├── 100-005-RTP-001_Free_Fall_Test_Protocol.html
│   │   ├── 100-005-RTP-002_Simulated_Transport_Test_Protocol.html
│   │   ├── 100-005-STP-001_Real-time_Aging_Stability_Plan.html
│   │   ├── 100-005-STP-002_Accelerated_Aging_Stability_Plan.html
│   │   ├── 100-005-CER-001_Clinical_Evaluation_Report.html
│   │   └── 100-005-VVE-001_VV_Test_Executive_Summary.html
│   │
│   ├── 04-design-output/            # 3 documents
│   │   ├── 100-005-DHF-001_DHF_Review_Checklist.html
│   │   ├── 100-005-DMR-001_DMR_Index_Review_Form.html
│   │   └── 100-005-IFU-001_Instructions_for_Use.html
│   │
│   ├── 07-materials-components/     # 9 documents
│   │   ├── 100-005-SIP-001_Front_Component_Inspection_Specification.html
│   │   ├── 100-005-SIP-011_Rear_Cover_Inspection_Specification.html
│   │   ├── 100-005-SIP-012_Actuation_Rod_Inspection_Specification.html
│   │   ├── 100-005-SIP-014_Push_Rod_Inspection_Specification.html
│   │   ├── 000-000-MRR-008_HYTREL_6356_Material_Review_Report.html
│   │   ├── 000-000-MRR-011_PC_ABS_Material_Review_Report.html
│   │   ├── 000-000-MRR-012_POM_FG500P_Material_Review_Report.html
│   │   └── 000-000-MRR-013_HF1130-111_Polycarbonate_Material_Review_Report.html
│   │
│   └── Audit_Corrective_Action_Report_2024.html  # ✅ Audit trail document
│
├── Excel/                            # BOM dashboard
│   └── 100-005-BOM-001_Interactive_EN.html
│
├── reference/                        # Reference documentation
│   ├── TEAM_MEMBERS_REFERENCE.md      # 17 team members database
│   ├── DHF_Document_Refinement_Review.md
│   └── Vem 审计文件清单.docx
│
└── archive/                          # 🗂️ ARCHIVED MATERIALS (not for audit)
    ├── backup_2026-01-14_pre-reorg/  # Pre-reorganization backup
    ├── sources/                       # Chinese markdown source files
    │   └── Vem audit doc markdown/
    ├── status_reports/                # All status/tracking reports
    ├── development_artifacts/         # Python/shell scripts, examples
    └── backup_files/                  # All .bak files
```

---

## 🔧 Execution Steps

### Step 1: Create Archive Structure
```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"

mkdir -p archive/{status_reports,development_artifacts,backup_files,sources}
```

### Step 2: Move Backup Files
```bash
# All .bak files
find documents/ -name "*.bak*" -type f -exec mv {} archive/backup_files/ \;

# Reference backup
mv reference/TEAM_MEMBERS_REFERENCE.md.backup archive/backup_files/

# Backup directory
mv backup_2026-01-14_pre-reorg archive/
```

### Step 3: Move Status Reports
```bash
mv AUDIT_DAY_CHECKLIST.md archive/status_reports/
mv SIGNATURE_*.md archive/status_reports/
mv PATH_FIXES_COMPLETE.md archive/status_reports/
mv FOLDER_REORGANIZATION_COMPLETE.md archive/status_reports/
mv GSPR_FINAL_VERIFICATION.md archive/status_reports/
mv VEM_AUDIT_LINK_STATUS_REPORT.md archive/status_reports/
mv final_signature_verification_report.md archive/status_reports/
mv README_AUDIT_SUMMARY.md archive/status_reports/
```

### Step 4: Move Development Scripts
```bash
mv analyze_signatures*.py archive/development_artifacts/
mv detailed_signature_analysis.py archive/development_artifacts/
mv final_summary.sh archive/development_artifacts/
mv fix_index_links.sh archive/development_artifacts/
mv signature-*.html archive/development_artifacts/
mv Excel/convert_bom_csv_to_html.py archive/development_artifacts/
```

### Step 5: Move Source Files
```bash
mv "Vem audit doc markdown" archive/sources/
mv .agent archive/ 2>/dev/null || true
mv .claude archive/ 2>/dev/null || true
```

### Step 6: Choose Index File
```bash
# Recommended: Use index_refined.html for MDR-compliant structure
# Option A: Keep index_refined.html, rename to index.html
mv index.html archive/development_artifacts/  # Backup old index
mv index_refined.html index.html  # Make refined the main index

# OR Option B: Keep both (add link to refined in main index)
# Keep both files, add link in index.html to index_refined.html
```

### Step 7: Update .gitignore
```bash
cat > .gitignore << 'EOF'
# System files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Backup files
*.bak
*.bak2
*.bak3
*.bak4
*~

# Claude/Agent temp files
.agent/
.claude/

# Archive directory (optional - comment out if you want to track archive)
# archive/
EOF
```

### Step 8: Git Status Check
```bash
git status
```

### Step 9: Review Before Commit
```bash
# Count production documents
find documents/ -name "*.html" ! -name "*.bak*" | wc -l

# Verify no .bak files remain
find documents/ -name "*.bak*"

# Check root directory clutter
ls -la | grep -v "^d" | grep -v "^total"
```

### Step 10: Commit to GitHub
```bash
git add .
git commit -m "🧹 Clean repository structure - Remove backup files and development artifacts

- Archive all .bak files (20 backup files)
- Archive status reports (15 tracking files)
- Archive development scripts (7 Python/shell files)
- Move source markdown to archive/sources/
- Use index_refined.html as main index (MDR-compliant structure)
- Update .gitignore for backup files

Production documents: 31 files (no .bak)
Archive: development history preserved"

git push origin main
```

---

## 📊 Before/After Comparison

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| **Root files** | 25 | 8 | ✅ -68% clutter |
| **Total .bak files** | 20 | 0 | ✅ 100% removed |
| **Production HTML** | 31 + 20 bak | 31 | ✅ Clean |
| **Status reports** | 15 (root) | 0 (root) | ✅ Archived |
| **Dev scripts** | 7 (root) | 0 (root) | ✅ Archived |
| **Git tracking** | Messy | Clean | ✅ Audit-ready |

---

## ⚠️ Critical Decisions Needed

### 1. Index File Choice
**Recommendation**: Use `index_refined.html` as main index
- ✅ MDR Annex II/III compliant structure
- ✅ ISO 13485 audit-friendly
- ✅ Logical flow (01-07 sections)

**Action**:
```bash
# Replace index.html with index_refined.html
mv index.html index_old.html  # Temporarily backup
mv index_refined.html index.html
git rm index_old.html
```

### 2. Audit Report Location
**Current**: `documents/Audit_Corrective_Action_Report_2024.html`

**Options**:
- **A**: Keep in `documents/` root ✅ RECOMMENDED (easy access)
- **B**: Move to new `08-audit-trail/` folder (more structured)
- **C**: Link from index.html "Audit Trail & Quality System" section

**Recommendation**: Keep current location, ensure index.html links to it

### 3. Archive Directory Tracking
**Decision**: Should `archive/` be tracked in Git?

**Pros**:
- ✅ Complete history preserved
- ✅ Source markdown available for reference
- ✅ Development artifacts documented

**Cons**:
- ❌ Larger repository size
- ❌ Clutter in git history

**Recommendation**: Track archive/ but add to .gitignore if size becomes issue

---

## ✅ Final Checklist

- [ ] All .bak files moved to archive/backup_files/
- [ ] All status reports moved to archive/status_reports/
- [ ] All dev scripts moved to archive/development_artifacts/
- [ ] Source markdown moved to archive/sources/
- [ ] .agent/ and .claude/ archived
- [ ] Index file chosen and renamed (if needed)
- [ ] .gitignore updated
- [ ] Git status checked
- [ ] Production documents verified (31 files)
- [ ] No .bak files in documents/
- [ ] Audit report linked from index.html
- [ ] README.md updated with archive location
- [ ] Committed to GitHub

---

## 🎯 Expected Result

**Clean GitHub Repository**:
- ✅ 31 production HTML documents (no .bak)
- ✅ Clear directory structure (01-07 folders)
- ✅ Root directory has only 8 files
- ✅ Archive preserves all development history
- ✅ Audit-ready for Vem Pharma
- ✅ ISO 13485 compliant
- ✅ MDR 2017/745 compliant

**Repository Size**: ~5-10 MB (reasonable for documentation)

---

## 📝 Post-Cleanup README Update

Add to README.md:

```markdown
## Archive Structure

Development history and source files preserved in `archive/`:
- `archive/sources/` - Chinese markdown source documents
- `archive/status_reports/` - Development progress reports (2026-01-12 to 2026-01-15)
- `archive/development_artifacts/` - Analysis scripts and examples
- `archive/backup_files/` - All .bak files (backup versions)
- `archive/backup_2026-01-14_pre-reorg/` - Pre-reorganization snapshot

Production documents in `documents/` folder are audit-ready.
```

---

**Status**: 📋 Plan ready for execution
**Next**: Execute cleanup steps 1-10 sequentially
**Time Estimate**: 15-20 minutes
**Risk**: Low (all files preserved in archive/)
