#!/bin/bash
###############################################################################
# SAFE GitHub Cleanup Script - Vem Audit Documentation
# Created: 2026-01-15
#
# FEATURES:
# - DRY-RUN mode (see what will happen without doing it)
# - Creates backup before cleanup
# - Moves files to archive/ (nothing deleted)
# - Complete rollback capability
###############################################################################

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
ARCHIVE_DIR="$PROJECT_DIR/archive"
DRY_RUN=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help)
            echo "Usage: $0 [--dry-run]"
            echo ""
            echo "Options:"
            echo "  --dry-run    Show what will happen without doing it"
            echo ""
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage"
            exit 1
            ;;
    esac
done

echo -e "${CYAN}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${CYAN}║     GitHub Cleanup - Vem Audit Documentation            ║${NC}"
echo -e "${CYAN}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}⚠️  DRY-RUN MODE${NC}"
    echo "No changes will be made - this shows what WILL happen"
    echo ""
fi

###############################################################################
# Pre-cleanup Check
###############################################################################
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📋 PRE-CLEANUP CHECKLIST${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Check for backup
if [ -f ".last_backup_location" ]; then
    BACKUP_PATH=$(cat .last_backup_location)
    if [ -d "$BACKUP_PATH" ]; then
        echo -e "${GREEN}✓ Backup found: $BACKUP_PATH${NC}"
    else
        echo -e "${YELLOW}⚠️  Backup location exists but directory missing${NC}"
        read -p "Create new backup now? (y/N) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            ./backup_before_cleanup.sh
        fi
    fi
else
    echo -e "${YELLOW}⚠️  No backup found${NC}"
    echo ""
    read -p "Create backup now? (RECOMMENDED) (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ./backup_before_cleanup.sh
    else
        echo -e "${RED}❌ Skipping backup (not recommended!)${NC}"
    fi
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}📊 CURRENT STATE ANALYSIS${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Count files
ROOT_FILES=$(ls -1 "$PROJECT_DIR" 2>/dev/null | grep -v "^\." | wc -l | tr -d ' ')
BAK_FILES=$(find "$PROJECT_DIR/documents" -name "*.bak*" 2>/dev/null | wc -l | tr -d ' ')
PROD_HTML=$(find "$PROJECT_DIR/documents" -name "*.html" ! -name "*.bak*" 2>/dev/null | wc -l | tr -d ' ')
STATUS_REPORTS=$(ls -1 "$PROJECT_DIR"/*.md 2>/dev/null | wc -l | tr -d ' ')
DEV_SCRIPTS=$(ls -1 "$PROJECT_DIR"/*.py "$PROJECT_DIR"/*.sh 2>/dev/null | wc -l | tr -d ' ')

echo -e "Current file counts:"
echo -e "  • Root files (excluding hidden): ${CYAN}$ROOT_FILES${NC}"
echo -e "  • Production HTML documents: ${CYAN}$PROD_HTML${NC}"
echo -e "  • .bak files: ${YELLOW}$BAK_FILES${NC}"
echo -e "  • Status reports (*.md): ${YELLOW}$STATUS_REPORTS${NC}"
echo -e "  • Dev scripts (*.py, *.sh): ${YELLOW}$DEV_SCRIPTS${NC}"
echo ""

# Show what will be done
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}🔍 DRY-RUN: What WILL Happen${NC}"
else
    echo -e "${GREEN}🚀 What WILL Happen${NC}"
fi
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo -e "Files to be moved:"
echo -e "  1. ${YELLOW}$BAK_FILES .bak files${NC} → ${GREEN}archive/backup_files/${NC}"
echo -e "  2. ${YELLOW}$STATUS_REPORTS status reports${NC} → ${GREEN}archive/status_reports/${NC}"
echo -e "  3. ${YELLOW}$DEV_SCRIPTS dev scripts${NC} → ${GREEN}archive/development_artifacts/${NC}"
echo -e "  4. ${YELLOW}Source markdown${NC} → ${GREEN}archive/sources/${NC}"
echo -e "  5. ${YELLOW}Temp directories${NC} → ${GREEN}archive/${NC}"
echo ""

# Expected result
NEW_ROOT_FILES=$((ROOT_FILES - BAK_FILES - STATUS_REPORTS - DEV_SCRIPTS - 2))
echo -e "Expected result:"
echo -e "  • Root files: ${CYAN}$ROOT_FILES${NC} → ${GREEN}$NEW_ROOT_FILES${NC}"
echo -e "  • .bak files: ${YELLOW}$BAK_FILES${NC} → ${GREEN}0${NC}"
echo -e "  • Production HTML: ${GREEN}$PROD_HTML${NC} (unchanged)"
echo ""

# Confirmation
if [ "$DRY_RUN" = false ]; then
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${RED}⚠️  READY TO EXECUTE${NC}"
    echo -e "${RED}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "This will MOVE files to archive/ (nothing deleted)"
    echo "All files can be restored from backup if needed"
    echo ""
    read -p "Continue with cleanup? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo -e "${RED}❌ Cleanup cancelled${NC}"
        exit 0
    fi
    echo ""
else
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${YELLOW}✅ DRY-RUN COMPLETE${NC}"
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    echo "To run actual cleanup:"
    echo "  ./cleanup_github_safe.sh"
    echo ""
    exit 0
fi

###############################################################################
# Execution
###############################################################################
cd "$PROJECT_DIR"

# Step 1: Create archive structure
echo -e "\n${GREEN}Step 1: Creating archive structure...${NC}"
if [ "$DRY_RUN" = false ]; then
    mkdir -p "$ARCHIVE_DIR"/{status_reports,development_artifacts,backup_files,sources}
fi
echo -e "${GREEN}✓ Archive directories created${NC}"

# Step 2: Move .bak files
echo -e "\n${GREEN}Step 2: Moving .bak files...${NC}"
if [ "$DRY_RUN" = false ]; then
    find documents/ -name "*.bak*" -type f -exec mv {} "$ARCHIVE_DIR/backup_files/" \;
    if [ -f "reference/TEAM_MEMBERS_REFERENCE.md.backup" ]; then
        mv reference/TEAM_MEMBERS_REFERENCE.md.backup "$ARCHIVE_DIR/backup_files/"
    fi
fi
echo -e "${GREEN}✓ Moved $BAK_COUNT .bak files${NC}"

# Step 3: Move status reports
echo -e "\n${GREEN}Step 3: Moving status reports...${NC}"
STATUS_REPORTS_LIST=(
    "AUDIT_DAY_CHECKLIST.md"
    "SIGNATURE_STATUS_REPORT.md"
    "SIGNATURE_CORRECTION_ACTION_PLAN.md"
    "SIGNATURE_UPDATES_COMPLETED.md"
    "PATH_FIXES_COMPLETE.md"
    "FOLDER_REORGANIZATION_COMPLETE.md"
    "GSPR_FINAL_VERIFICATION.md"
    "VEM_AUDIT_LINK_STATUS_REPORT.md"
    "final_signature_verification_report.md"
    "README_AUDIT_SUMMARY.md"
)

if [ "$DRY_RUN" = false ]; then
    for report in "${STATUS_REPORTS_LIST[@]}"; do
        [ -f "$report" ] && mv "$report" "$ARCHIVE_DIR/status_reports/"
    done
fi
echo -e "${GREEN}✓ Moved status reports${NC}"

# Step 4: Move development scripts
echo -e "\n${GREEN}Step 4: Moving development scripts...${NC}"
DEV_SCRIPTS_LIST=(
    "analyze_signatures.py"
    "analyze_signatures_fixed.py"
    "detailed_signature_analysis.py"
    "final_summary.sh"
    "fix_index_links.sh"
    "signature-dashboard-example.html"
    "signature-example-enhanced.html"
)

if [ "$DRY_RUN" = false ]; then
    for script in "${DEV_SCRIPTS_LIST[@]}"; do
        [ -f "$script" ] && mv "$script" "$ARCHIVE_DIR/development_artifacts/"
    done
    [ -f "Excel/convert_bom_csv_to_html.py" ] && mv Excel/convert_bom_csv_to_html.py "$ARCHIVE_DIR/development_artifacts/"
fi
echo -e "${GREEN}✓ Moved development scripts${NC}"

# Step 5: Move source files
echo -e "\n${GREEN}Step 5: Moving source files...${NC}"
if [ "$DRY_RUN" = false ]; then
    [ -d "Vem audit doc markdown" ] && mv "Vem audit doc markdown" "$ARCHIVE_DIR/sources/"
    [ -d ".agent" ] && mv .agent "$ARCHIVE_DIR/"
    [ -d ".claude" ] && mv .claude "$ARCHIVE_DIR/"
    [ -d "backup_2026-01-14_pre-reorg" ] && mv backup_2026-01-14_pre-reorg "$ARCHIVE_DIR/"
fi
echo -e "${GREEN}✓ Moved source files and temp directories${NC}"

# Step 6: Index file choice
echo -e "\n${GREEN}Step 6: Index file selection...${NC}"
echo ""
echo "Which index file to use?"
echo "  1) index_refined.html (MDR-compliant, recommended for audit) ✅"
echo "  2) Keep both files"
echo "  3) Keep index.html as-is"
echo ""
read -p "Choose (1/2/3) [1]: " INDEX_CHOICE
INDEX_CHOICE=${INDEX_CHOICE:-1}

if [ "$DRY_RUN" = false ]; then
    case $INDEX_CHOICE in
        1)
            mv index.html "$ARCHIVE_DIR/development_artifacts/index_old.html"
            mv index_refined.html index.html
            echo -e "${GREEN}✓ Using index_refined.html as main index${NC}"
            ;;
        2)
            echo -e "${GREEN}✓ Keeping both index files${NC}"
            ;;
        3)
            mv index_refined.html "$ARCHIVE_DIR/development_artifacts/"
            echo -e "${GREEN}✓ Keeping index.html, archived index_refined.html${NC}"
            ;;
    esac
fi

# Step 7: Update .gitignore
echo -e "\n${GREEN}Step 7: Updating .gitignore...${NC}"
if [ "$DRY_RUN" = false ]; then
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

# Optional: Track archive for complete history
# archive/
EOF
fi
echo -e "${GREEN}✓ .gitignore updated${NC}"

###############################################################################
# Verification
###############################################################################
echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}✅ VERIFICATION${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

# Count results
NEW_BAK_COUNT=$(find documents/ -name "*.bak*" 2>/dev/null | wc -l | tr -d ' ')
NEW_PROD_COUNT=$(find documents/ -name "*.html" ! -name "*.bak*" 2>/dev/null | wc -l | tr -d ' ')
NEW_ROOT_COUNT=$(ls -1 "$PROJECT_DIR" 2>/dev/null | grep -v "^\." | wc -l | tr -d ' ')

echo -e "Results:"
echo -e "  • Production HTML: ${GREEN}$NEW_PROD_COUNT${NC} documents"
echo -e "  • .bak files remaining: ${GREEN}$NEW_BAK_COUNT${NC}"
echo -e "  • Root files: ${GREEN}$NEW_ROOT_COUNT${NC}"
echo ""

# Check for problems
PROBLEMS=0

if [ "$NEW_BAK_COUNT" -gt 0 ]; then
    echo -e "${RED}⚠️  Warning: $NEW_BAK_COUNT .bak files still present${NC}"
    find documents/ -name "*.bak*" | head -5
    ((PROBLEMS++))
fi

if [ "$NEW_PROD_COUNT" -ne 31 ]; then
    echo -e "${YELLOW}⚠️  Expected 31 production documents, found $NEW_PROD_COUNT${NC}"
    ((PROBLEMS++))
fi

if [ $PROBLEMS -eq 0 ]; then
    echo -e "${GREEN}✅ All checks passed!${NC}"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}🎉 CLEANUP COMPLETE!${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${CYAN}Next steps:${NC}"
echo "  1. 🧪 Test in browser:"
echo "     open index.html"
echo ""
echo "  2. 🔍 Verify links work"
echo ""
echo "  3. 📊 Check git status:"
echo "     git status"
echo ""
echo "  4. ✅ Commit when ready:"
echo "     git add ."
echo "     git commit -m '🧹 Clean repository structure'"
echo "     git push origin main"
echo ""
echo -e "${GREEN}💾 Backup available at: $BACKUP_PATH${NC}"
echo -e "${GREEN}📖 Restore instructions: $BACKUP_PATH/RESTORE_INSTRUCTIONS.txt${NC}"
echo ""
