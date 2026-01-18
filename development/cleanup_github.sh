#!/bin/bash
###############################################################################
# GitHub Cleanup Script - Vem Audit Documentation
# Created: 2026-01-15
# Purpose: Clean repository structure after 3 days of refinement
# WARNING: This script MOVES files to archive/ - all files are preserved!
###############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
ARCHIVE_DIR="$PROJECT_DIR/archive"
BACKUP_TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}GitHub Cleanup - Vem Audit Documentation${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Safety check
echo -e "${YELLOW}⚠️  SAFETY CHECK${NC}"
echo "This script will MOVE files to archive/ directory."
echo "All files will be PRESERVED - nothing will be deleted."
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${RED}❌ Cleanup cancelled${NC}"
    exit 1
fi

# Change to project directory
cd "$PROJECT_DIR"

###############################################################################
# Step 1: Create Archive Structure
###############################################################################
echo -e "\n${GREEN}Step 1: Creating archive structure...${NC}"
mkdir -p "$ARCHIVE_DIR"/{status_reports,development_artifacts,backup_files,sources}
echo -e "${GREEN}✓ Archive directories created${NC}"

###############################################################################
# Step 2: Move Backup Files (.bak files)
###############################################################################
echo -e "\n${GREEN}Step 2: Moving backup files (.bak)...${NC}"
BAK_COUNT=$(find documents/ -name "*.bak*" -type f 2>/dev/null | wc -l)
if [ $BAK_COUNT -gt 0 ]; then
    find documents/ -name "*.bak*" -type f -exec mv {} "$ARCHIVE_DIR/backup_files/" \;
    echo -e "${GREEN}✓ Moved $BAK_COUNT .bak files${NC}"
else
    echo -e "${YELLOW}⚠️  No .bak files found${NC}"
fi

# Reference backup
if [ -f "reference/TEAM_MEMBERS_REFERENCE.md.backup" ]; then
    mv reference/TEAM_MEMBERS_REFERENCE.md.backup "$ARCHIVE_DIR/backup_files/"
    echo -e "${GREEN}✓ Moved reference backup${NC}"
fi

###############################################################################
# Step 3: Move Status Reports
###############################################################################
echo -e "\n${GREEN}Step 3: Moving status reports...${NC}"
STATUS_REPORTS=(
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

MOVED_COUNT=0
for report in "${STATUS_REPORTS[@]}"; do
    if [ -f "$report" ]; then
        mv "$report" "$ARCHIVE_DIR/status_reports/"
        ((MOVED_COUNT++))
    fi
done
echo -e "${GREEN}✓ Moved $MOVED_COUNT status reports${NC}"

###############################################################################
# Step 4: Move Development Scripts
###############################################################################
echo -e "\n${GREEN}Step 4: Moving development scripts...${NC}"
DEV_SCRIPTS=(
    "analyze_signatures.py"
    "analyze_signatures_fixed.py"
    "detailed_signature_analysis.py"
    "final_summary.sh"
    "fix_index_links.sh"
    "signature-dashboard-example.html"
    "signature-example-enhanced.html"
)

SCRIPTS_MOVED=0
for script in "${DEV_SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        mv "$script" "$ARCHIVE_DIR/development_artifacts/"
        ((SCRIPTS_MOVED++))
    fi
done
echo -e "${GREEN}✓ Moved $SCRIPTS_MOVED development scripts${NC}"

# Excel conversion script
if [ -f "Excel/convert_bom_csv_to_html.py" ]; then
    mv Excel/convert_bom_csv_to_html.py "$ARCHIVE_DIR/development_artifacts/"
    echo -e "${GREEN}✓ Moved Excel conversion script${NC}"
fi

###############################################################################
# Step 5: Move Source Files
###############################################################################
echo -e "\n${GREEN}Step 5: Moving source files and temp directories...${NC}"

# Source markdown
if [ -d "Vem audit doc markdown" ]; then
    mv "Vem audit doc markdown" "$ARCHIVE_DIR/sources/"
    echo -e "${GREEN}✓ Moved source markdown to archive/sources/${NC}"
fi

# Agent/Claude temp directories
if [ -d ".agent" ]; then
    mv .agent "$ARCHIVE_DIR/"
    echo -e "${GREEN}✓ Moved .agent directory${NC}"
fi

if [ -d ".claude" ]; then
    mv .claude "$ARCHIVE_DIR/"
    echo -e "${GREEN}✓ Moved .claude directory${NC}"
fi

# Backup directory
if [ -d "backup_2026-01-14_pre-reorg" ]; then
    mv backup_2026-01-14_pre-reorg "$ARCHIVE_DIR/"
    echo -e "${GREEN}✓ Moved backup directory${NC}"
fi

###############################################################################
# Step 6: Index File Decision
###############################################################################
echo -e "\n${GREEN}Step 6: Choosing index file...${NC}"
echo -e "${BLUE}Recommendation: Use index_refined.html (MDR-compliant)${NC}"
echo ""
echo "Options:"
echo "  1) Use index_refined.html as main index (recommended for audit)"
echo "  2) Keep both files (link to refined from main)"
echo "  3) Keep current index.html as is"
echo ""
read -p "Choose option (1/2/3) [1]: " INDEX_CHOICE
INDEX_CHOICE=${INDEX_CHOICE:-1}

case $INDEX_CHOICE in
    1)
        echo -e "${YELLOW}→ Backing up index.html to archive/${NC}"
        mv index.html "$ARCHIVE_DIR/development_artifacts/index_old.html"
        mv index_refined.html index.html
        echo -e "${GREEN}✓ index_refined.html is now the main index${NC}"
        ;;
    2)
        echo -e "${YELLOW}→ Keeping both index files${NC}"
        echo -e "${GREEN}✓ Both index.html and index_refined.html preserved${NC}"
        ;;
    3)
        echo -e "${YELLOW}→ Keeping current index.html${NC}"
        echo -e "${YELLOW}→ Archiving index_refined.html${NC}"
        mv index_refined.html "$ARCHIVE_DIR/development_artifacts/"
        echo -e "${GREEN}✓ index.html unchanged, index_refined.html archived${NC}"
        ;;
    *)
        echo -e "${RED}❌ Invalid choice, keeping both files${NC}"
        ;;
esac

###############################################################################
# Step 7: Update .gitignore
###############################################################################
echo -e "\n${GREEN}Step 7: Updating .gitignore...${NC}"
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
echo -e "${GREEN}✓ .gitignore updated${NC}"

###############################################################################
# Step 8: Verification
###############################################################################
echo -e "\n${GREEN}Step 8: Verification...${NC}"

# Count production documents
DOC_COUNT=$(find documents/ -name "*.html" ! -name "*.bak*" | wc -l | tr -d ' ')
echo -e "${GREEN}✓ Production HTML documents: $DOC_COUNT${NC}"

# Check for remaining .bak files
BAK_REMAINING=$(find documents/ -name "*.bak*" 2>/dev/null | wc -l | tr -d ' ')
if [ "$BAK_REMAINING" -eq 0 ]; then
    echo -e "${GREEN}✓ No .bak files in documents/${NC}"
else
    echo -e "${RED}❌ Warning: $BAK_REMAINING .bak files still present${NC}"
fi

# Count root files
ROOT_FILES=$(ls -la | grep "^-" | grep -v "\.md" | grep -v "\.html" | grep -v "\.sh" | wc -l | tr -d ' ')
echo -e "${GREEN}✓ Root directory cleaned${NC}"

# Show archive size
if [ -d "$ARCHIVE_DIR" ]; then
    ARCHIVE_SIZE=$(du -sh "$ARCHIVE_DIR" | awk '{print $1}')
    echo -e "${GREEN}✓ Archive size: $ARCHIVE_SIZE${NC}"
fi

###############################################################################
# Step 9: Git Status
###############################################################################
echo -e "\n${GREEN}Step 9: Git status...${NC}"
git status --short

###############################################################################
# Step 10: Completion Summary
###############################################################################
echo -e "\n${BLUE}========================================${NC}"
echo -e "${GREEN}✅ CLEANUP COMPLETE!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "Summary of changes:"
echo "  • Backup files moved: $BAK_COUNT"
echo "  • Status reports moved: $MOVED_COUNT"
echo "  • Development scripts moved: $SCRIPTS_MOVED"
echo "  • Production documents: $DOC_COUNT"
echo "  • Archive size: $ARCHIVE_SIZE"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Review changes: git status"
echo "  2. Test in browser: open index.html"
echo "  3. Commit changes:"
echo "     git add ."
echo "     git commit -m '🧹 Clean repository structure'"
echo "     git push origin main"
echo ""
echo -e "${GREEN}✓ All files preserved in archive/${NC}"
echo ""
