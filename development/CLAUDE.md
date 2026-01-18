# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Project**: Summed Medtech 森迈医疗 - Vem Pharma Audit Documentation System
**Purpose**: Design History File (DHF) preparation for regulatory audit
**Product**: Epinephrine Auto-Injector (SM100-005 Lisa Adult, SM100-006 Lucy Pediatric)
**Customer**: Vem Pharma Turkey (regulatory audit preparation)
**Status**: 32/32 documents complete (100%), production-ready
**Repository**: https://github.com/AlexCHONG8/Vem.git
**Workflow**: Chinese source → English HTML with ISO13485:2016 & FDA 21 CFR 820 compliance

---

## Quick Commands

### Document Management
```bash
# Count total HTML documents
find documents/ -name "*.html" | grep -v ".bak" | wc -l

# Count documents by category
for dir in documents/*/; do echo "$dir: $(find "$dir" -name "*.html" | grep -v ".bak" | wc -l | tr -d ' ')"; done

# Validate English output (should return nothing)
grep -rP '[\x{4e00}-\x{9fff}]' documents/ --include="*.html" | grep -v ".bak"

# Open document in browser (macOS)
open documents/01-risk-management/100-005-RMP-001_Risk_Management_Plan.html
```

### Quality Checks
```bash
# Check CSS links (all should point to ../../assets/css/)
grep -r "stylesheet" documents/ --include="*.html" | grep -v ".bak" | grep -v "../../assets/css/"

# Check image paths (all should point to ../../assets/images/)
grep -r "img src" documents/ --include="*.html" | grep -v ".bak" | grep -v "../../assets/images/"

# Verify medical device terminology
grep -r "Epinephrine" documents/ --include="*.html" | grep -v ".bak" | wc -l

# Check signature format (horizontal 3-column, no thead)
grep -r "signature-table" documents/ --include="*.html" | grep -v ".bak" | grep -c "thead"
```

### Git Operations
```bash
# Check repository status
git status --short

# Create commit (always use detailed messages)
git add .
git commit -m "📝 [Brief description]

- [Change 1]
- [Change 2]
- [Impact/Reason]"

# Push to GitHub
git push origin main
```

---

## Architecture Overview

### Document Structure (32 HTML files in 5 categories)

```
documents/
├── 01-risk-management/         # 6 documents (RMP, PFA, DFA, UFM, RAC, SPR)
├── 02-design-input/            # 4 documents (URS, PRS, MAT, PSC)
├── 03-design-verification/     # 9 documents (BEP, FTP, RTP x2, STP x2, DVP, CER, VVE)
├── 04-design-output/           # 3 documents (DHF, DMR, IFU)
├── 07-materials-components/    # 9 documents (BOM, MRR x4, SIP x4)
└── Audit_Corrective_Action_Report_2024.html
```

### Conversion Pipeline

```
Chinese Source → Markdown Extraction → English Translation → HTML Generation → Browser Review → Word Export
```

**Key Points**:
- Source files in `"Vem audit doc markdown/"` (archived after conversion)
- HTML output in `documents/[category]/`
- All documents follow identical header/signature structure
- User manually exports HTML to Word after browser review

### CSS Architecture

**Master Stylesheet**: `assets/css/summed-medtech-docs.css` (233 lines)

**Critical Classes**:
- `.a4-container` - A4 page simulation (210mm width, 5% margins, 15mm padding)
- `.header-section` - Flexbox layout for logo + document metadata
- `.company-logo` - Summed logo (styled with inline `width: 80% !important; max-width: 300px !important; height: auto !important;`)
- `.signature-table` - Horizontal 3-column layout (single `<tr>`, NO `<thead>`)
- `.doc-info-table` - Document metadata tables (25%-15%-30%-30% column split)
- `.revision-table` - Revision history tracking

**Typography**:
- Font: Google Fonts `Inter` (wght@400;500;600;700)
- Responsive zoom: 150% (≥1400px), 125% (1100-1399px), 100% (<1099px)

---

## Critical Standards (Non-Negotiable)

### 1. Header Format (RMP-Style - All Documents Must Match)

```html
<div class="header-section">
    <img src="../../assets/images/Summed logo.png"
         alt="Summed Medtech 森迈医疗"
         class="company-logo"
         style="width: 80% !important; max-width: 300px !important; height: auto !important;">
    <div class="document-meta">
        <div><strong>Document No.:</strong> [100-005-XXX-001]</div>
        <div><strong>Revision:</strong> [1.0]</div>
    </div>
</div>

<h1>[Document Type] ([Code])</h1>
<h2>[Document Subtitle]</h2>

<table class="doc-info-table">
    <tr>
        <td width="25%"><strong>Document No.:</strong></td>
        <td colspan="3">[100-005-XXX-001]</td>
    </tr>
    <tr>
        <td><strong>Revision:</strong></td>
        <td>[1.0]</td>
        <td><strong>Effective Date:</strong></td>
        <td>[YYYY-MM-DD]</td>
    </tr>
    <tr>
        <td><strong>Prepared by:</strong></td>
        <td colspan="3">[Name]</td>
    </tr>
</table>
```

**CRITICAL**: Logo must use inline styles with `!important` flags to override CSS defaults.

### 2. Digital Signature Format (21 CFR Part 11 Compliant)

**Standard Format** (RMP-Style, Multi-Row):
```html
<table class="doc-info-table">
    <tr>
        <td rowspan="2" width="15%"><strong>Prepared by</strong></td>
        <td width="25%"><strong>Preparer:</strong> /s/ [English Name]</td>
        <td width="30%"><strong>Signature:</strong> ____________________</td>
    </tr>
    <tr>
        <td><strong>Department:</strong> [Department Name]</td>
        <td><strong>Date:</strong> ____________________</td>
    </tr>
    <!-- Additional reviewers follow same pattern -->
</table>
```

**Alternative Horizontal 3-Column** (Simplified documents):
```html
<table class="signature-table">
<tr>
  <td>
    <div class="signature-block">
      <div class="signature-name">/s/ [Name]</div>
      <div class="signature-title">[Job Title]</div>
      <div class="signature-line"></div>
      <div class="signature-label">Prepared by</div>
    </div>
  </td>
  <td><!-- Reviewed by --></td>
  <td><!-- Approved by --></td>
</tr>
</table>
```

**Rules**:
- Format: `/s/ [English Name]` (NEVER handwritten images)
- Use ONLY names from original Chinese source document
- Map Chinese names to `reference/TEAM_MEMBERS_REFERENCE.md` English names
- NO `<thead>` section in signature tables

### 3. Medical Device English Standards

**Capitalization**:
- Drug names: **Epinephrine** (always capitalized)
- Device names: **Auto-Injector** (capitalized, hyphenated)
- Product models: **Lisa**, **Lucy**, **Simject** (always capitalized)
- Document codes: **SM100-005**, **SM100-006** (SM prefix required)

**Spacing** (space BEFORE unit, no space AFTER symbols):
- Volume: `0.3 mL`, `0.27 mg` (space between number and unit)
- Force: `5-35 N`, `5-25 N` (space after N)
- Time: `≤ 24 h`, `≤ 2 seconds` (space after number, before unit)
- Symbols: `≤ 80%`, `≥ 0.4 in`, `± 0.03 mL` (space after symbol)
- Tool names: `Lisa & Lucy` (spaces around & symbol)

### 4. File Path Standards

**Relative Paths** (from `documents/[category]/`):
- CSS: `../../assets/css/summed-medtech-docs.css` (up 2 levels)
- Images: `../../assets/images/[filename]` (up 2 levels)
- Root-level files: `../../[filename]` (up 2 levels)

**From root-level** (e.g., `index.html`):
- CSS: `assets/css/summed-medtech-docs.css`
- Images: `assets/images/[filename]`

---

## Team Member Database (CRITICAL)

**Location**: `reference/TEAM_MEMBERS_REFERENCE.md` (17 team members, v3.3)

**Critical Mappings** (common errors):
| Chinese Name | Correct English Name | ID |
|--------------|---------------------|-------|
| 张福昌 | Alex Chong (NOT Andy Tsai) | BD001 |
| 杨荣壬 | Zen Yang | QM001 |
| 赵佃佳 | Logan Zhao | RD002 |
| 薛媛媛 | Grace Xue | RA001 |
| 张琪裴 | Doris Chang | BD002 |
| 高张昀 | ZY Gao | PD002 (resigned 2025-04-30) |

**Usage Pattern**:
1. Read Chinese source document signature table
2. Find Chinese names (`zh_name` in TEAM_MEMBERS_REFERENCE.md)
3. Extract corresponding English name (`en_name`)
4. Use ONLY English names in HTML: `/s/ [English Name]`
5. If name not in source, DO NOT add it

---

## Document Type Codes

| Code | English | Chinese | Approval Chain |
|------|---------|---------|----------------|
| RMP | Risk Management Plan | 风险管理计划 | RD002 → QM001 → GM001 |
| PFA | Process FMEA | 过程失效模式分析 | RD003 → QA001 → RD002 |
| DFA | Design FMEA | 设计失效模式分析 | RD003 → QA001 → RD002 |
| UFM | Use FMEA | 使用者失效模式分析 | RA001 → BD002 → GM001 |
| URS | User Requirement Specification | 用户需求说明书 | RD003 → QM001 → PD001 |
| PRS | Product Requirement Specification | 产品需求说明书 | RD003 → QM001 → PD001 |
| BEP | Biological Evaluation Plan | 生物相容性评估计划 | RD003 → RD002 → QM001 |
| FTP | Functional Test Plan | 功能测试计划 | RD003 → QA001 → RD002 |
| RTP | Reliability Test Protocol | 可靠性试验方案 | RD003 → QA001 → RD002 |
| STP | Stability Test Plan | 稳定性试验方案 | RD003 → QA001 → RD002 |
| IFU | Instructions for Use | 使用说明书 | RA001 → QM001 → GM001 |
| BOM | Bill of Materials | 物料清单 | RD002 → QA001 → RD001 |

**Full matrix**: See `approval_matrix` in `reference/TEAM_MEMBERS_REFERENCE.md`

---

## Common Issues & Solutions

### Issue: Logo Not Displaying Properly
**Cause**: Wrong image path or missing inline styles
**Solution**:
```html
<!-- CORRECT -->
<img src="../../assets/images/Summed logo.png"
     class="company-logo"
     style="width: 80% !important; max-width: 300px !important; height: auto !important;">
```

### Issue: Chinese Characters Remain
**Detection**: `grep -rP '[\x{4e00}-\x{9fff}]' documents/`
**Solution**: Re-translate affected sections, verify all text is English

### Issue: Wrong Signature Format
**Detection**: `grep "thead" documents/*/[filename] | grep signature`
**Solution**: Convert to horizontal 3-column format (remove `<thead>`)

### Issue: BOM Dashboard Header Doesn't Match RMP
**Detection**: Visual comparison shows logo too small/missing h2 subtitle
**Solution**: Ensure both h1 and h2 present, logo has inline styles

### Issue: Broken CSS/Image Links
**Detection**: Browser console shows 404 errors
**Solution**: Verify relative paths (should be `../../assets/...` from documents/ subfolders)

---

## File Organization

**Production Files** (DO NOT modify without reason):
- `documents/**/*.html` - Final HTML documents (32 files)
- `assets/css/summed-medtech-docs.css` - Master stylesheet
- `assets/images/*` - Logos, diagrams, figures
- `reference/TEAM_MEMBERS_REFERENCE.md` - Team database (source of truth)

**Archived Files** (reference only):
- `archive/` - Backup of old versions, source markdown, development artifacts
- `Excel/` - Source spreadsheets (BOM 2.0, org charts)
- `"Vem audit doc markdown/"` - Chinese source files (37 files)

**Root-Level** (navigation and reference):
- `index.html` - Main navigation dashboard (MDR 2017/745 Annex II/III structure)
- `README.md` - Project overview and quick start
- `CLAUDE.md` - This file
- `Summed_Org_Chart.html` - Organization chart
- `Simject_Assembly_Flowchart.html` - Assembly process flowchart

### Root-Level Files Details

**index.html** - Navigation Dashboard
- **Purpose**: Main entry point for browsing all DHF documents
- **Structure**: Organized by MDR 2017/745 Annex II/III categories
- **Usage**: Open in browser to navigate between documents
- **Links**: All relative paths to `documents/` subfolders

**Simject_Assembly_Flowchart.html** - Process Visualization
- **Purpose**: Visual representation of assembly process flow
- **Usage**: Reference for manufacturing process understanding
- **Image**: `assets/images/Simject assembly flowchart.png`

**Summed_Org_Chart.html** - Organization Structure
- **Purpose**: Company hierarchy and reporting structure
- **Usage**: Reference for organizational authority
- **Image**: Summed org chart visualization

---

## When Updating Documents

### Scenario 1: Correcting Team Member Names
1. Read original Chinese source document
2. Extract Chinese names from signature table
3. Match to `reference/TEAM_MEMBERS_REFERENCE.md` `zh_name` field
4. Replace with `en_name` from same record
5. Update `title` field if needed
6. Verify signature format: `/s/ [English Name]`
7. Validate: `grep -rP '[\x{4e00}-\x{9fff}]' [filename]`

### Scenario 2: Fixing Header Format to Match RMP
1. Ensure logo has inline styles: `style="width: 80% !important; max-width: 300px !important; height: auto !important;"`
2. Verify h1 title format: `[Document Type] ([Code])`
3. Add h2 subtitle if missing: `[Document Subtitle]`
4. Check doc-info-table has 3 rows (Document No, Revision + Effective Date, Prepared by)
5. Verify logo path: `../../assets/images/Summed logo.png` (from documents/ subfolders)

### Scenario 3: Reorganizing Folders
1. Create backup: `backup_YYYY-MM-DD-description/`
2. Move files with `git mv` to preserve history
3. Update all relative path references
4. Test in browser after moves
5. Update `index.html` links if needed
6. Commit with detailed message

---

## Browser Testing & Validation

### Testing Documents in Browser

Before considering any document complete, always test in browser:

```bash
# Open document in default browser (macOS)
open documents/01-risk-management/100-005-RMP-001_Risk_Management_Plan.html

# Open with specific browser (macOS)
open -a "Google Chrome" documents/[category]/[filename].html
open -a "Safari" documents/[category]/[filename].html
open -a "Microsoft Edge" documents/[category]/[filename].html
```

### Visual Validation Checklist

**Header Section**:
- [ ] Summed logo displays at correct size (80%, 300px max)
- [ ] Document No. and Revision visible in header
- [ ] h1 title format: `[Document Type] ([Code])`
- [ ] h2 subtitle present (not empty)

**Content Sections**:
- [ ] All text is English (no Chinese characters)
- [ ] Medical device terminology correct (Epinephrine, Auto-Injector)
- [ ] Unit spacing correct (0.3 mL, 5-35 N, ≤ 24 h)
- [ ] Tables render with proper column widths
- [ ] Images load correctly (check browser console for 404s)

**Signature Section**:
- [ ] Signature format: `/s/ [English Name]` (not handwritten images)
- [ ] Team members match source document (no additions)
- [ ] Signature table uses horizontal 3-column format (no `<thead>`)
- [ ] Job titles correct from `reference/TEAM_MEMBERS_REFERENCE.md`

**CSS Rendering**:
- [ ] Page displays with A4 width simulation
- [ ] Responsive zoom applies (150%/125%/100% based on screen size)
- [ ] Print preview shows correct page breaks
- [ ] No horizontal scrollbars at normal zoom

### Console Error Checking

Open browser Developer Tools (Cmd+Option+I on macOS) and check:

**Console Tab**:
- Look for 404 errors (missing CSS or images)
- Check for JavaScript errors (should be none - documents are static HTML)
- Verify no CSS parsing errors

**Network Tab**:
- Verify CSS loads: `../../assets/css/summed-medtech-docs.css`
- Verify images load: `../../assets/images/[filename]`

### Common Browser Issues

**Problem**: Logo doesn't display
- **Cause**: Wrong relative path or missing inline styles
- **Fix**: Check path is `../../assets/images/Summed logo.png`, verify inline styles present

**Problem**: CSS not applying
- **Cause**: Wrong relative path
- **Fix**: From `documents/[category]/`, path should be `../../assets/css/summed-medtech-docs.css`

**Problem**: Horizontal scrollbar appears
- **Cause**: Content exceeds A4 width
- **Fix**: Reduce image sizes, adjust table column widths, check for long URLs

**Problem**: Print preview shows extra blank pages
- **Cause**: Missing or misplaced `<div class="page-break"></div>`
- **Fix**: Place page breaks between major sections only

---

## Git Workflow

### Before Committing
1. **Validate quality**: Run grep commands to check for Chinese, broken links
2. **Test in browser**: Open modified files, verify rendering
3. **Check status**: `git status --short` to review changes
4. **Diff review**: `git diff [filename]` for specific file changes

### Commit Message Format
```bash
git commit -m "📝 [Type] [Brief description]

- [Change 1]
- [Change 2]
- [Change 3]

Impact: [What this fixes/improves]
Refs: [Related documents or issues]"
```

### Example Commits
```bash
# Document update
git commit -m "📝 Update RMP-001 header to match standard format

- Add inline styles to logo (80%, 300px max)
- Add h2 subtitle: Auto-Injector Risk Management Plan
- Fix signature table to RMP format (multi-row with departments)
- Update revision history table

Impact: Ensures RMP header matches all other documents
Refs: documents/01-risk-management/"

# Reorganization
git commit -m "🔧 Move MRR and SIP documents to 07-materials-components/

- Move 4 MRR files from 04-design-output/ to 07-materials-components/
- Move 4 SIP files from 04-design-output/ to 07-materials-components/
- Update index.html links to reflect new locations
- Create backup at backup_2026-01-14_pre-reorg/

Impact: Aligns folder structure with DHF phase organization
Refs: index.html, documents/07-materials-components/"
```

---

## Working with index.html

### Understanding index.html Structure

**Purpose**: Main navigation dashboard for all DHF documents
**Structure**: Organized by MDR 2017/745 Annex II/III categories
**Location**: Repository root level

### Updating index.html Links

When adding, moving, or renaming documents:

```bash
# 1. Find the document's current link in index.html
grep -n "100-005-RTP-001" index.html

# 2. Update the href path to match new location
# Old: href="documents/03-design-verification/100-005-RTP-001_Free_Fall_Test_Protocol.html"
# New: href="documents/[new-category]/100-005-RTP-001_Free_Fall_Test_Protocol.html"

# 3. Verify link works in browser
open index.html
# Click the link to confirm it opens the correct document
```

### Adding New Documents to index.html

When creating a new document:

```html
<!-- Add link in appropriate category section -->
<li>
    <a href="documents/[category]/[Document_Code]_[Document_Title].html">
        <strong>[CODE]</strong> [Document Type] - [Document Title]
    </a>
</li>
```

**Example**:
```html
<li>
    <a href="documents/03-design-verification/100-005-RTP-003_Vibration_Test_Protocol.html">
        <strong>RTP-003</strong> Reliability Test Protocol - Vibration Test Protocol
    </a>
</li>
```

### Validating index.html

```bash
# Check for broken links (requires Python)
python3 -c "
import os
from pathlib import Path
from bs4 import BeautifulSoup

with open('index.html') as f:
    soup = BeautifulSoup(f, 'html.parser')
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('documents/'):
            if not Path(href).exists():
                print(f'BROKEN: {href}')
"

# Verify all document counts match
echo "Expected total: $(grep -c 'documents/' index.html)"
echo "Actual files: $(find documents/ -name '*.html' | wc -l)"
```

---

## Key Reference Documents

### Essential Reading for All Work
1. **`reference/TEAM_MEMBERS_REFERENCE.md`** - Team database (17 members, approval matrix)
2. **`assets/css/summed-medtech-docs.css`** - CSS architecture and styling rules
3. **`README.md`** - Project overview, document index, compliance matrix

### Example Documents (Copy Format From)
1. **RMP** (`documents/01-risk-management/100-005-RMP-001_Risk_Management_Plan.html`) - Complete header/signature format
2. **BOM** (`documents/07-materials-components/100-005-BOM-001_Dashboard.html`) - Interactive dashboard with collapse/tree
3. **IFU** (`documents/04-design-output/100-005-IFU-001_Instructions_for_Use.html`) - 14-section structure with figures
4. **index.html** (root level) - Navigation dashboard structure reference

### Troubleshooting Guides
- **Header Issues**: Compare with RMP header structure
- **Signature Issues**: Check `reference/TEAM_MEMBERS_REFERENCE.md` for correct names
- **Path Issues**: Verify `../../assets/` relative paths from documents/ subfolders

---

## Production-Ready Checklist

Before considering any document complete, verify:

- [ ] 100% English (no Chinese characters)
- [ ] Logo displays with proper size (80%, 300px max, inline styles)
- [ ] Header matches RMP format (h1 + h2, doc-info-table)
- [ ] Signatures use `/s/ [English Name]` format
- [ ] Team members from source document only (not added)
- [ ] CSS link works: `../../assets/css/summed-medtech-docs.css`
- [ ] Images load: `../../assets/images/[filename]`
- [ ] Medical device terminology correct (Epinephrine, Auto-Injector)
- [ ] Unit spacing correct (0.3 mL, 5-35 N, ≤ 24 h)
- [ ] Digital signature format 21 CFR Part 11 compliant
- [ ] Opens correctly in browser (test with `open [filename]`)

---

**Last Updated**: 2026-01-16
**Repository**: https://github.com/AlexCHONG8/Vem.git
**Status**: Production-ready, 32/32 documents complete (100%)
**Audit Target**: Vem Pharma Turkey regulatory audit

---

## Repository Structure Summary

```
Vem audit/                          # Root repository (GitHub: AlexCHONG8/Vem)
├── index.html                      # Main navigation dashboard (START HERE)
├── README.md                       # Project overview and quick start
├── CLAUDE.md                       # This file - Claude Code guidance
├── Simject_Assembly_Flowchart.html # Assembly process visualization
├── Summed_Org_Chart.html           # Organization structure chart
│
├── documents/                      # 32 HTML documents (production output)
│   ├── 01-risk-management/         # 6 documents (RMP, PFA, DFA, UFM, RAC, SPR)
│   ├── 02-design-input/            # 4 documents (URS, PRS, MAT, PSC)
│   ├── 03-design-verification/     # 9 documents (BEP, FTP, RTP x2, STP x2, DVP, CER, VVE)
│   ├── 04-design-output/           # 3 documents (DHF, DMR, IFU)
│   ├── 07-materials-components/    # 9 documents (BOM, MRR x4, SIP x4)
│   └── Audit_Corrective_Action_Report_2024.html
│
├── assets/
│   ├── css/summed-medtech-docs.css # Master stylesheet (A4, print-ready)
│   └── images/                     # Logos, diagrams, figures (28 files)
│
├── reference/
│   ├── TEAM_MEMBERS_REFERENCE.md   # 17 team members + approval matrix (v3.3)
│   └── dhf-reference.md            # DHF document types reference (100+ types)
│
├── archive/                        # Backup directories and old versions
├── Excel/                          # Source spreadsheets (BOM 2.0, org charts)
├── claudedocs/                     # Claude-generated reports and analyses
└── [cleanup scripts]               # Various bash scripts for maintenance
```
