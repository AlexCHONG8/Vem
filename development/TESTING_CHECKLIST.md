# 🔒 SAFE TESTING CHECKLIST
**Before Cleanup - Don't Skip This!**

---

## 📋 Testing Philosophy

**Rule #1**: Test safely FIRST, then cleanup
**Rule #2**: If anything breaks, you CAN revert
**Rule #3**: Never commit to git until you've tested everything

---

## 🚀 Step-by-Step Testing Process

### Phase 1: Pre-Cleanup Backup (5 minutes)

```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
./backup_before_cleanup.sh
```

**What this does:**
- ✅ Creates complete snapshot in parent directory
- ✅ Timestamp: `snapshot_before_cleanup_20260115_143022`
- ✅ Saves restore instructions
- ✅ Location: `.last_backup_location`

**Verify backup:**
```bash
# Check backup was created
cat .last_backup_location

# Verify backup exists
ls -la ../snapshot_before_cleanup_*/

# Count files in backup
find ../snapshot_before_cleanup_* -type f | wc -l
```

✅ **Checkpoint**: Backup created and verified

---

### Phase 2: Dry-Run Testing (2 minutes)

```bash
./cleanup_github_safe.sh --dry-run
```

**What this does:**
- ✅ Shows exactly what WILL happen
- ✅ NO changes made
- ✅ Shows file counts before/after

**Expected output:**
```
📊 CURRENT STATE ANALYSIS
  • Root files: 25
  • Production HTML documents: 31
  • .bak files: 20
  • Status reports: 15
  • Dev scripts: 7

🔍 DRY-RUN: What WILL Happen
Files to be moved:
  1. 20 .bak files → archive/backup_files/
  2. 15 status reports → archive/status_reports/
  3. 7 dev scripts → archive/development_artifacts/
  4. Source markdown → archive/sources/
  5. Temp directories → archive/

Expected result:
  • Root files: 25 → 8
  • .bak files: 20 → 0
  • Production HTML: 31 (unchanged)
```

✅ **Checkpoint**: Dry-run looks correct

---

### Phase 3: Actual Cleanup (3 minutes)

```bash
./cleanup_github_safe.sh
```

**Interactive prompts:**
1. Backup check - should find your backup
2. Index file choice - choose option 1 (recommended)
3. Confirmation - type 'y' to proceed

**What happens:**
- ✅ All .bak files moved
- ✅ Status reports archived
- ✅ Dev scripts archived
- ✅ Source files archived
- ✅ .gitignore updated
- ✅ Index file chosen

✅ **Checkpoint**: Cleanup completed without errors

---

### Phase 4: Post-Cleanup Verification (5 minutes)

#### 4.1 Count Production Documents
```bash
find documents/ -name "*.html" ! -name "*.bak*" | wc -l
```
**Expected**: 31

#### 4.2 Check for .bak Files
```bash
find documents/ -name "*.bak*"
```
**Expected**: (empty - no results)

#### 4.3 List Root Directory
```bash
ls -la | grep "^-"
```
**Expected files:**
- CLAUDE.md
- README.md
- index.html
- Summed_Org_Chart.html
- Simject_Assembly_Flowchart.html
- backup_before_cleanup.sh
- cleanup_github_safe.sh
- (Plus testing markdown files)

#### 4.4 Verify Archive Structure
```bash
ls -la archive/
```
**Expected directories:**
- backup_files/ (20+ .bak files)
- status_reports/ (10+ .md files)
- development_artifacts/ (7+ files)
- sources/ (Vem audit doc markdown/)
- snapshot_before_cleanup_*/
- .agent/ (if existed)
- .claude/ (if existed)

#### 4.5 Check Archive File Count
```bash
echo "Backup files: $(find archive/backup_files/ -type f | wc -l)"
echo "Status reports: $(find archive/status_reports/ -type f | wc -l)"
echo "Dev artifacts: $(find archive/development_artifacts/ -type f | wc -l)"
echo "Source files: $(find archive/sources/ -type f | wc -l)"
```

**Expected:**
- Backup files: 20+
- Status reports: 10+
- Dev artifacts: 7+
- Source files: 50+

✅ **Checkpoint**: All file counts correct

---

### Phase 5: Browser Testing (CRITICAL - 5 minutes)

#### 5.1 Open Index File
```bash
open index.html
# OR double-click in Finder
```

#### 5.2 Test Quick Links (Top of Page)
Click each link and verify:
- [ ] **🏢 Organization Chart** → Opens Summed_Org_Chart.html
- [ ] **⚙️ Assembly Flowchart** → Opens Simject_Assembly_Flowchart.html
- [ ] **📜 ISO 13485 Certificate** → Opens PDF
- [ ] **🎥 Virtual Anji Plant Tour** → Opens video

#### 5.3 Test Phase Links
Click through each phase and verify links work:
- [ ] Phase 1: Risk Management (6 documents)
- [ ] Phase 2: Design Input (4 documents)
- [ ] Phase 3: Design Verification (9 documents)
- [ ] Phase 4: Design Output (3 documents)
- [ ] Phase 5: Materials (9 documents)
- [ ] Audit Trail section (1 document)

**Sample test:**
```
Click: 100-005-RMP-001_Risk_Management_Plan.html
Expected: Opens in browser, loads correctly
```

#### 5.4 Test Footer Links
- [ ] Organization Chart
- [ ] Assembly Flowchart
- [ ] ISO 13485 Certificate
- [ ] Virtual Plant Tour

✅ **Checkpoint**: All links work in browser

---

### Phase 6: Git Verification (2 minutes)

```bash
# Check git status
git status
```

**Expected output:**
```
Changes not staged for commit:
  modified:   .gitignore
  deleted:    documents/xxx.html.bak
  deleted:    AUDIT_DAY_CHECKLIST.md
  ...
  renamed:    index_refined.html -> index.html
```

**Key things to verify:**
- ✅ Production HTML files NOT deleted (only .bak files)
- ✅ .bak files show as "deleted"
- ✅ Status reports show as "deleted"
- ✅ archive/ directory shows as "untracked"

✅ **Checkpoint**: Git status looks correct

---

### Phase 7: Rollback Test (OPTIONAL - Advanced)

**Test rollback capability (don't actually do it, just verify you CAN):**

```bash
# Read restore instructions
cat ../snapshot_before_cleanup_*/RESTORE_INSTRUCTIONS.txt

# Verify backup has all files
ls ../snapshot_before_cleanup_*/documents/*.html | wc -l
```

**Expected**: Backup has all original files

✅ **Checkpoint**: You know how to restore if needed

---

## 🎯 Decision Time

### ✅ All Tests Passed? Proceed to Git!

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
Archive: development history preserved
All links tested and working"

git push origin main
```

### ❌ Something Broke? Rollback!

**Option 1: Restore from backup**
```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/"
mv "Vem audit" "Vem audit.broken"
cp -R snapshot_before_cleanup_* "Vem audit"
```

**Option 2: Git reset**
```bash
# Reset to before cleanup (if not yet pushed)
git reset --hard HEAD

# OR soft reset (keep changes)
git reset --soft HEAD~1
```

**Option 3: Manual restore**
```bash
# Copy specific files from backup
cp ../snapshot_before_cleanup_*/documents/xxx.html.bak documents/
```

---

## 📊 Testing Results Template

```
Testing Date: _______________
Tester Name: _______________

Phase 1: Backup Created  ✅ / ❌
Phase 2: Dry-Run Passed   ✅ / ❌
Phase 3: Cleanup Complete ✅ / ❌
Phase 4: File Counts OK   ✅ / ❌
Phase 5: Browser Test     ✅ / ❌
Phase 6: Git Status OK    ✅ / ❌

Overall Result: ✅ PASS / ❌ FAIL

Notes:
_________________________
_________________________
_________________________
```

---

## ⚠️ Warning Signs

**STOP if you see:**
- ❌ Production HTML files deleted (only .bak should move)
- ❌ Less than 31 HTML files in documents/
- ❌ index.html doesn't load in browser
- ❌ Links broken (404 errors)
- ❌ Git shows unexpected deletions

**DO NOT proceed to git commit until all tests pass!**

---

## 🆘 Emergency Contacts

**If something goes wrong:**
1. Check backup: `cat .last_backup_location`
2. Read restore instructions: `[BACKUP]/RESTORE_INSTRUCTIONS.txt`
3. Use rollback section above
4. Restore from git: `git reset --hard HEAD`

---

## ✅ Final Checklist Before Git Push

- [ ] Backup created and verified
- [ ] Dry-run completed successfully
- [ ] Cleanup completed without errors
- [ ] File counts correct (31 production, 0 .bak)
- [ ] Browser testing passed (all links work)
- [ ] Git status looks correct
- [ ] NO production files deleted
- [ ] Archive directory created correctly
- [ ] Index file loads and links work
- [ ] Commit message written clearly

**All checked? You're ready to push!** 🚀

---

**Remember**: Nothing is permanent until you `git push`!
- Local changes can be reset anytime
- Backup provides complete restore capability
- Test thoroughly before pushing
