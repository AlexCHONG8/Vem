# 🚀 SAFE CLEANUP - QUICK START
**Vem Audit Documentation - GitHub Upload Preparation**

---

## 📖 Overview

**Safety First**: You have 100% rollback capability
- ✅ Complete backup before anything happens
- ✅ Dry-run mode to see what will happen
- ✅ Nothing deleted (only moved to archive)
- ✅ Easy restore if something breaks

---

## ⚡ 3 Simple Steps

### Step 1: Create Backup (5 min) 🔒
```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
./backup_before_cleanup.sh
```

**Result**: Complete snapshot created
- Location: `../snapshot_before_cleanup_20260115_HHMMSS/`
- All files preserved exactly as they are now
- Restore instructions included

✅ **Verify**: `cat .last_backup_location`

---

### Step 2: Test with Dry-Run (2 min) 🔍
```bash
./cleanup_github_safe.sh --dry-run
```

**Result**: See what will happen without doing it
```
📊 CURRENT STATE:
  Root files: 25
  .bak files: 20
  Production HTML: 31

🔍 WHAT WILL HAPPEN:
  20 .bak files → archive/backup_files/
  15 status reports → archive/status_reports/
  7 dev scripts → archive/development_artifacts/
  Source files → archive/sources/

✅ EXPECTED RESULT:
  Root files: 25 → 8
  .bak files: 20 → 0
  Production HTML: 31 (unchanged)
```

✅ **Verify**: Numbers look correct? Proceed to Step 3.

---

### Step 3: Run Cleanup (3 min) 🧹
```bash
./cleanup_github_safe.sh
```

**Interactive prompts:**
1. ✅ Backup found? Yes
2. ✅ Index file choice? Choose **1** (recommended)
3. ✅ Continue? Type **y**

**Result:**
- All .bak files moved to archive/
- All status reports moved to archive/
- All dev scripts moved to archive/
- Root directory cleaned (8 files remaining)
- Production documents untouched (31 files)

✅ **Verify**: `find documents/ -name "*.bak*"` (should be empty)

---

## 🧪 Phase 4: Testing (CRITICAL - 5 min)

### Test 1: Count Files
```bash
find documents/ -name "*.html" ! -name "*.bak*" | wc -l
```
**Expected**: 31

### Test 2: Check for .bak Files
```bash
find documents/ -name "*.bak*"
```
**Expected**: (empty)

### Test 3: Open in Browser
```bash
open index.html
```

**Test all links:**
- [ ] Organization Chart loads
- [ ] Assembly Flowchart loads
- [ ] ISO Certificate opens
- [ ] Virtual Tour plays
- [ ] Phase links work (click a few)
- [ ] Document links work (click a few)

### Test 4: Git Status
```bash
git status
```

**Should show:**
- ✅ .bak files deleted
- ✅ Status reports deleted
- ✅ Dev scripts deleted
- ✅ archive/ directory new
- ✅ Production HTML untouched

---

## ✅ All Tests Passed? Time for Git!

```bash
git add .
git commit -m "🧹 Clean repository structure - Remove backup files

- Archive all .bak files (20 backup files)
- Archive status reports (15 tracking files)
- Archive development scripts (7 Python/shell files)
- Move source markdown to archive/sources/
- Use index_refined.html as main index (MDR-compliant)
- Update .gitignore for backup files

Production: 31 HTML documents (clean)
Archive: Complete history preserved
All links tested and working"

git push origin main
```

---

## 🔄 Rollback (If Something Breaks)

### Option 1: Quick Restore from Backup
```bash
cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/"
mv "Vem audit" "Vem audit.broken.$(date +%Y%m%d)"
cp -R snapshot_before_cleanup_* "Vem audit"
```

### Option 2: Git Reset (Before Push)
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# OR undo everything (lose changes)
git reset --hard HEAD~1
```

### Option 3: Restore Specific Files
```bash
# Restore specific .bak file
cp ../snapshot_before_cleanup_*/documents/xxx.html.bak documents/
```

---

## 📊 Before vs After

| Metric | Before | After |
|--------|--------|-------|
| **Root files** | 25 | 8 |
| **.bak files** | 20 | 0 |
| **Production HTML** | 31 | 31 |
| **Status reports** | 15 (root) | 0 (root) |
| **Dev scripts** | 7 (root) | 0 (root) |
| **Git tracking** | Messy | Clean |
| **Audit ready?** | No | ✅ Yes |

---

## 📁 Final Structure

```
Vem audit/
├── .git/
├── .gitignore (updated)
├── .last_backup_location
│
├── index.html (MDR-compliant)
├── Summed_Org_Chart.html
├── Simject_Assembly_Flowchart.html
│
├── assets/ (images, css)
├── documents/ (31 production HTML - NO .bak)
│   ├── 01-risk-management/
│   ├── 02-design-input/
│   ├── 03-design-verification/
│   ├── 04-design-output/
│   ├── 07-materials-components/
│   └── Audit_Corrective_Action_Report_2024.html
│
├── Excel/ (BOM dashboard)
├── reference/ (team members, docs)
│
└── archive/ (all cleanup targets)
    ├── backup_files/ (20 .bak files)
    ├── status_reports/ (15 .md files)
    ├── development_artifacts/ (7 scripts)
    ├── sources/ (37 markdown files)
    └── snapshot_before_cleanup_*/
```

---

## 🎯 Success Criteria

You're successful when:
- ✅ `find documents/ -name "*.bak*"` returns nothing
- ✅ `find documents/ -name "*.html" ! -name "*.bak*" | wc -l` returns 31
- ✅ index.html opens in browser and all links work
- ✅ Organization Chart and Flowchart load
- ✅ Git status shows clean changes
- ✅ You have backup location saved

---

## ⚠️ Common Issues

### Issue: Script permission denied
**Fix**: `chmod +x backup_before_cleanup.sh cleanup_github_safe.sh`

### Issue: .last_backup_location not found
**Fix**: Run backup script first, it creates this file

### Issue: Links broken in browser
**Fix**: Clear browser cache, try again

### Issue: Git shows unexpected deletions
**Fix**: Check that only .bak and report files deleted, NOT production HTML

---

## 📞 Help

**Commands to check status:**
```bash
# Check backup
cat .last_backup_location

# Count files
find documents/ -name "*.html" ! -name "*.bak*" | wc -l

# Check for .bak
find documents/ -name "*.bak*"

# Git status
git status

# Open in browser
open index.html
```

---

## ✅ Ready?

1. **Backup**: `./backup_before_cleanup.sh`
2. **Dry-run**: `./cleanup_github_safe.sh --dry-run`
3. **Cleanup**: `./cleanup_github_safe.sh`
4. **Test**: Open index.html, click links
5. **Commit**: `git add . && git commit -m "..." && git push`

**You're 100% safe - backup guarantees rollback!** 🛡️
