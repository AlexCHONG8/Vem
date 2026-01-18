#!/bin/bash

# Fix Script for index.html Link Issues
# Generated: 2026-01-14
# Author: Claude Code
# Purpose: Fix broken and incorrect links in index.html

INDEX_FILE="index.html"
BACKUP_FILE="index_backup_$(date +%Y%m%d_%H%M%S).html"

echo "=========================================="
echo "Vem Audit index.html Link Fix Script"
echo "=========================================="
echo ""

# Create backup
echo "📦 Creating backup: $BACKUP_FILE"
cp "$INDEX_FILE" "$BACKUP_FILE"
echo "✅ Backup created successfully"
echo ""

# Fix 1: BOM Interactive Link (Line 612)
echo "🔧 Fix 1: BOM Interactive link path"
echo "   Old: documents/07-materials-components/100-005-BOM-001_Interactive_EN.html"
echo "   New: Excel/100-005-BOM-001_Interactive_EN.html"
sed -i '' 's|href="documents/07-materials-components/100-005-BOM-001_Interactive_EN.html"|href="Excel/100-005-BOM-001_Interactive_EN.html"|g' "$INDEX_FILE"
echo "✅ Fixed"
echo ""

# Fix 2: SPR-001 GSPR Link (Line 679)
echo "🔧 Fix 2: SPR-001 GSPR filename (add _CHECKLIST suffix)"
echo "   Old: 100-005-SPR-001_General_Safety_and_Performance_Requirements.html"
echo "   New: 100-005-SPR-001_General_Safety_and_Performance_Requirements_CHECKLIST.html"
sed -i '' 's|100-005-SPR-001_General_Safety_and_Performance_Requirements\.html|100-005-SPR-001_General_Safety_and_Performance_Requirements_CHECKLIST.html|g' "$INDEX_FILE"
echo "✅ Fixed"
echo ""

# Fix 3: SIP Document Paths (Lines 620-650)
echo "🔧 Fix 3: SIP-001 Front Component path (04 → 07)"
sed -i '' 's|documents/04-design-output/100-005-SIP-001_Front_Component_Inspection_Specification\.html|documents/07-materials-components/100-005-SIP-001_Front_Component_Inspection_Specification.html|g' "$INDEX_FILE"

echo "🔧 Fix 4: SIP-011 Rear Cover path (04 → 07)"
sed -i '' 's|documents/04-design-output/100-005-SIP-011_Rear_Cover_Inspection_Specification\.html|documents/07-materials-components/100-005-SIP-011_Rear_Cover_Inspection_Specification.html|g' "$INDEX_FILE"

echo "🔧 Fix 5: SIP-012 Actuation Rod path (04 → 07)"
sed -i '' 's|documents/04-design-output/100-005-SIP-012_Actuation_Rod_Inspection_Specification\.html|documents/07-materials-components/100-005-SIP-012_Actuation_Rod_Inspection_Specification.html|g' "$INDEX_FILE"

echo "🔧 Fix 6: SIP-014 Push Rod path (04 → 07)"
sed -i '' 's|documents/04-design-output/100-005-SIP-014_Push_Rod_Inspection_Specification\.html|documents/07-materials-components/100-005-SIP-014_Push_Rod_Inspection_Specification.html|g' "$INDEX_FILE"

echo "✅ All 4 SIP paths fixed"
echo ""

# Fix 4: MRR Document Paths (Lines 838-869)
echo "🔧 Fix 7: MRR-008 Hytrel path (02 → 07)"
sed -i '' 's|documents/02-design-input/000-000-MRR-008_HYTREL_6356_Material_Review_Report\.html|documents/07-materials-components/000-000-MRR-008_HYTREL_6356_Material_Review_Report.html|g' "$INDEX_FILE"

echo "🔧 Fix 8: MRR-011 PC+ABS path (02 → 07)"
sed -i '' 's|documents/02-design-input/000-000-MRR-011_PC_ABS_Material_Review_Report\.html|documents/07-materials-components/000-000-MRR-011_PC_ABS_Material_Review_Report.html|g' "$INDEX_FILE"

echo "🔧 Fix 9: MRR-012 POM path (02 → 07)"
sed -i '' 's|documents/02-design-input/000-000-MRR-012_POM_FG500P_Material_Review_Report\.html|documents/07-materials-components/000-000-MRR-012_POM_FG500P_Material_Review_Report.html|g' "$INDEX_FILE"

echo "🔧 Fix 10: MRR-013 Polycarbonate path (02 → 07)"
sed -i '' 's|documents/02-design-input/000-000-MRR-013_HF1130-111_Polycarbonate_Material_Review_Report\.html|documents/07-materials-components/000-000-MRR-013_HF1130-111_Polycarbonate_Material_Review_Report.html|g' "$INDEX_FILE"

echo "✅ All 4 MRR paths fixed"
echo ""

echo "=========================================="
echo "✅ ALL FIXES APPLIED SUCCESSFULLY"
echo "=========================================="
echo ""
echo "Summary:"
echo "  - Fixed 1 broken BOM link"
echo "  - Fixed 1 SPR-001 filename"
echo "  - Fixed 4 SIP document paths"
echo "  - Fixed 4 MRR document paths"
echo "  - Total: 10 link fixes applied"
echo ""
echo "Backup saved as: $BACKUP_FILE"
echo ""
echo "Next steps:"
echo "1. Open index.html in browser to verify all links work"
echo "2. Test each link by clicking through to documents"
echo "3. Add missing documents (PSC-001, VVE-001) to index if desired"
echo ""
echo "📋 Full report: VEM_AUDIT_LINK_STATUS_REPORT.md"
echo ""
