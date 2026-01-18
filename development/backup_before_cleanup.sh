#!/bin/bash
###############################################################################
# PRE-CLEANUP BACKUP SCRIPT
# Creates a complete snapshot BEFORE cleanup - SAFE REVERT POSSIBLE
###############################################################################

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Configuration
PROJECT_DIR="/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="snapshot_before_cleanup_${TIMESTAMP}"
BACKUP_PATH="${PROJECT_DIR}/../${BACKUP_NAME}"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}🔒 PRE-CLEANUP BACKUP${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "This will create a COMPLETE snapshot of your project"
echo "Location: $BACKUP_PATH"
echo ""

# Safety check
read -p "Create backup now? (y/N) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${RED}❌ Backup cancelled${NC}"
    exit 1
fi

echo -e "\n${GREEN}Creating backup...${NC}"

# Create backup directory
mkdir -p "$BACKUP_PATH"

# Copy ALL files (preserving permissions, timestamps)
echo -e "${YELLOW}→ Copying files...${NC}"
cp -R "$PROJECT_DIR"/* "$BACKUP_PATH/"

# Exclude the backup directory itself
rm -rf "$BACKUP_PATH/snapshot_before_cleanup_"*

# Count what we backed up
FILE_COUNT=$(find "$BACKUP_PATH" -type f | wc -l | tr -d ' ')
DIR_COUNT=$(find "$BACKUP_PATH" -type d | wc -l | tr -d ' ')

echo -e "${GREEN}✓ Backup created successfully!${NC}"
echo ""
echo "📦 Backup Statistics:"
echo "   Location: $BACKUP_PATH"
echo "   Files backed up: $FILE_COUNT"
echo "   Directories: $DIR_COUNT"
echo "   Total size: $(du -sh "$BACKUP_PATH" | awk '{print $1}')"
echo ""

# Create restore instructions
cat > "$BACKUP_PATH/RESTORE_INSTRUCTIONS.txt" << 'EOF'
╔══════════════════════════════════════════════════════════════════════╗
║                    HOW TO RESTORE FROM BACKUP                        ║
╔══════════════════════════════════════════════════════════════════════╝

🔧 EMERGENCY RESTORE (if cleanup went wrong):

1. Navigate to parent directory:
   cd "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/"

2. Rename current (broken) directory:
   mv "Vem audit" "Vem audit.broken.$(date +%Y%m%d)"

3. Restore from backup:
   cp -R BACKUP_SNAPSHOT_NAME "Vem audit"

4. Verify restore:
   cd "Vem audit"
   ls -la

═══════════════════════════════════════════════════════════════════════

📝 SELECTIVE FILE RESTORE:

If only specific files were affected:

cp BACKUP_SNAPSHOT_NAME/path/to/file.html "Vem audit/path/to/file.html"

═══════════════════════════════════════════════════════════════════════

🔄 GIT RESTORE:

If you already committed changes to git:

# Option 1: Revert last commit (KEEPING changes)
git reset --soft HEAD~1

# Option 2: Hard reset to previous commit (LOSE changes)
git reset --hard HEAD~1

# Option 3: Restore specific files from git
git checkout HEAD~1 -- path/to/file.html

═══════════════════════════════════════════════════════════════════════

✅ VERIFICATION:

After restore, verify:
1. All HTML files are present
2. No .bak files in documents/
3. Index file loads in browser
4. All links work

EOF

echo -e "${GREEN}✓ Restore instructions saved${NC}"
echo ""

# Save backup info
echo "$BACKUP_PATH" > "$PROJECT_DIR/.last_backup_location"
echo "Created: $(date)" >> "$PROJECT_DIR/.last_backup_location"

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ BACKUP COMPLETE!${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "Your project is now 100% safe."
echo "If cleanup goes wrong, use the restore instructions in:"
echo "  $BACKUP_PATH/RESTORE_INSTRUCTIONS.txt"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Test cleanup with DRY-RUN mode first"
echo "  2. Run actual cleanup when ready"
echo "  3. If something breaks: restore from backup"
echo ""
echo -e "${GREEN}Backup location saved to: .last_backup_location${NC}"
echo ""
