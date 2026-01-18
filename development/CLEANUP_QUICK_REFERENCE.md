# GitHub Cleanup Quick Reference
**Vem Audit Documentation - Post-Refinement Cleanup**

---

## 🚀 Quick Start (Automated)

```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
./cleanup_github.sh
```

**The script will:**
- ✅ Move all .bak files to archive/backup_files/
- ✅ Move status reports to archive/status_reports/
- ✅ Move development scripts to archive/development_artifacts/
- ✅ Move source markdown to archive/sources/
- ✅ Update .gitignore
- ✅ Ask which index file to use
- ✅ Show verification summary

---

## 📋 Manual Cleanup Steps (If You Prefer Control)

### 1. Create Archive Structure
```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
mkdir -p archive/{status_reports,development_artifacts,backup_files,sources}
```

### 2. Remove All .bak Files
```bash
# Find and count .bak files first
find documents/ -name "*.bak*"

# Move all .bak files to archive
find documents/ -name "*.bak*" -exec mv {} archive/backup_files/ \;

# Also move reference backup
mv reference/TEAM_MEMBERS_REFERENCE.md.backup archive/backup_files/
```

### 3. Archive Status Reports
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

### 4. Archive Development Scripts
```bash
mv analyze_signatures*.py archive/development_artifacts/
mv detailed_signature_analysis.py archive/development_artifacts/
mv *_summary.sh archive/development_artifacts/
mv signature-*.html archive/development_artifacts/
mv Excel/convert_bom_csv_to_html.py archive/development_artifacts/
```

### 5. Archive Source Files
```bash
mv "Vem audit doc markdown" archive/sources/
mv .agent archive/ 2>/dev/null || true
mv .claude archive/ 2>/dev/null || true
mv backup_2026-01-14_pre-reorg archive/
```

### 6. Choose Index File

**Option A: Use index_refined.html (Recommended for Audit)**
```bash
mv index.html archive/development_artifacts/index_old.html
mv index_refined.html index.html
```

**Option B: Keep Both**
```bash
# No action needed - both files remain
```

**Option C: Keep index.html Only**
```bash
mv index_refined.html archive/development_artifacts/
```

### 7. Update .gitignore
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

# Optional: Comment out below line if you want to track archive
# archive/
EOF
```

### 8. Verify Cleanup
```bash
# Count production documents (should be 31)
find documents/ -name "*.html" ! -name "*.bak*" | wc -l

# Check for remaining .bak files (should be 0)
find documents/ -name "*.bak*"

# Check git status
git status
```

### 9. Commit to GitHub
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

## ✅ Verification Checklist

After cleanup, verify:

- [ ] **Root directory** has only 8-10 files:
  - CLAUDE.md
  - README.md
  - index.html (or index.html + index_refined.html)
  - Summed_Org_Chart.html
  - Simject_Assembly_Flowchart.html
  - cleanup_github.sh (can delete after use)
  - GITHUB_CLEANUP_PLAN.md (can delete after use)
  - CLEANUP_QUICK_REFERENCE.md (can delete after use)

- [ ] **No .bak files** in documents/
  ```bash
  find documents/ -name "*.bak*"  # Should return nothing
  ```

- [ ] **Production documents** count is 31
  ```bash
  find documents/ -name "*.html" ! -name "*.bak*" | wc -l  # Should be 31
  ```

- [ ] **Archive directory** exists with:
  - archive/backup_files/ (20+ .bak files)
  - archive/status_reports/ (10+ .md files)
  - archive/development_artifacts/ (7+ files)
  - archive/sources/Vem audit doc markdown/ (37+ .md files)

- [ ] **Git status** shows clean changes
  ```bash
  git status
  ```

- [ ] **Test in browser**: Open index.html and verify links work

---

## 🎯 About the Audit Report

**Current location**: `documents/Audit_Corrective_Action_Report_2024.html`

**This is the correct location** because:
- ✅ It's a production document (not a backup)
- ✅ It's referenced in the audit trail
- ✅ It's accessible from the main index
- ✅ It fits with the "Audit Trail & Quality System" section

**DO NOT move this file** to archive/ - it's part of the production documentation.

---

## 📊 Expected Results

| Metric | Before | After |
|--------|--------|-------|
| Root files | 25 | 8 |
| .bak files | 20 | 0 |
| Production HTML | 31 | 31 |
| Repository size | ~15 MB | ~5-10 MB |

---

## 🔙 How to Undo

If something goes wrong, all files are in `archive/`:

```bash
# Restore .bak files
cp archive/backup_files/*.bak documents/*/

# Restore status reports
cp archive/status_reports/*.md ./

# Restore development scripts
cp archive/development_artifacts/*.{py,sh,html} ./

# Restore source files
cp -r archive/sources/"Vem audit doc markdown" ./

# Then: git checkout . to revert git changes
```

---

## ⚠️ Important Notes

1. **Nothing is deleted** - all files moved to `archive/`
2. **Git will track** the move (not delete + add)
3. **Commit message** should be descriptive for history
4. **Test thoroughly** before pushing to GitHub
5. **Audit report** stays in documents/ (don't archive)

---

**Need help?** Run `./cleanup_github.sh` - it's safe and guided!
