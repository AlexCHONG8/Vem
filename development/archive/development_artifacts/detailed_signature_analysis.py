#!/usr/bin/env python3
import os
import re
from pathlib import Path

def extract_all_signature_info(file_path):
    """Extract all signature-related information from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all signature blocks
        signature_pattern = r'<div class="signature-name[^"]*">([^<]+)</div>\s*<div class="signature-title">([^<]+)</div>\s*<div class="signature-label">([^<]+)</div>'
        matches = re.findall(signature_pattern, content, re.DOTALL)
        
        # Find all signature names with broader pattern
        name_pattern = r'<div class="signature-name[^"]*">([^<]+)</div>'
        all_names = re.findall(name_pattern, content)
        
        # Check for format issues
        has_thead = 'thead' in content and 'signature-table' in content
        has_single_tr = '<tr>' in content and '</tr>' in content
        
        # Check for Chinese characters
        chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
        has_chinese = any(chinese_pattern.search(name) for name in all_names)
        
        # Check for resigned names
        resigned_names = [
            '/s/ Coco Xu', '/s/ Logan Zhao', '/s/ Jimmy Xu',
            '/s/ Doris Chang', '/s/ Alex Chong', '/s/ Kevin Lo',
            '/s/ Zen Yang', '/s/ Jimmy Xu', '/s/ Anya Xiang',
            '/s/ Yanghua Su', '/s/ Zhangyun Gao', '/s/ Rongren Yang',
            '/s/ Chenjun Weng', '/s/ Dianjia Zhao', '/s/ Pengtao Gao',
            'Kayla Li', 'ZZ Huang', 'Nic Weng', 'Alvin Gao'
        ]
        
        has_resigned = any(name in all_names for name in resigned_names)
        
        return {
            'file': os.path.basename(file_path),
            'signatures': matches,
            'all_names': all_names,
            'has_chinese': has_chinese,
            'has_resigned': has_resigned,
            'format_issues': {
                'has_thead': has_thead,
                'has_single_tr': has_single_tr
            },
            'compliance_score': 0
        }
    except Exception as e:
        return {
            'file': os.path.basename(file_path),
            'error': str(e),
            'compliance_score': 0
        }

def calculate_compliance_score(info):
    """Calculate compliance score for each file"""
    score = 100
    
    if 'error' in info:
        score = 0
    
    if info['has_chinese']:
        score -= 50  # Major issue
    
    if info['has_resigned']:
        score -= 30  # Moderate issue - using resigned people
    
    if info['format_issues']['has_thead']:
        score -= 20  # Format issue - should be horizontal
    
    if not info['signatures']:
        score -= 100  # No signatures
    
    info['compliance_score'] = max(0, score)
    return info

def main():
    documents_dir = Path("documents")
    html_files = list(documents_dir.glob("*.html")) + list(documents_dir.rglob("*.html"))
    
    print("=" * 100)
    print("COMPREHENSIVE SIGNATURE ANALYSIS REPORT")
    print("=" * 100)
    
    results = []
    high_priority = []
    medium_priority = []
    low_priority = []
    no_issues = []
    
    for html_file in sorted(html_files):
        info = extract_all_signature_info(html_file)
        info = calculate_compliance_score(info)
        results.append(info)
        
        if info['compliance_score'] == 0:
            no_issues.append(info)
        elif info['compliance_score'] <= 30:
            high_priority.append(info)
        elif info['compliance_score'] <= 70:
            medium_priority.append(info)
        else:
            low_priority.append(info)
    
    # Print summary
    print(f"\n📊 SUMMARY STATISTICS")
    print("-" * 100)
    print(f"Total HTML files analyzed: {len(results)}")
    print(f"Files with no issues: {len(no_issues)}")
    print(f"Files requiring attention: {len(high_priority) + len(medium_priority)}")
    print(f"  - High priority (≤30): {len(high_priority)}")
    print(f"  - Medium priority (31-70): {len(medium_priority)}")
    print(f"  - Low priority (71-99): {len(low_priority)}")
    
    # Detailed high priority issues
    if high_priority:
        print(f"\n🚨 HIGH PRIORITY ISSUES (Compliance Score ≤ 30)")
        print("-" * 100)
        for info in high_priority:
            print(f"\n📁 {info['file']}")
            print(f"   Score: {info['compliance_score']}/100")
            
            if info['has_chinese']:
                print(f"   ⚠️  Contains Chinese characters in signatures")
            if info['has_resigned']:
                print(f"   ⚠️  Contains resigned personnel signatures")
            if info['format_issues']['has_thead']:
                print(f"   ⚠️  Uses vertical signature format (needs conversion)")
            if not info['signatures']:
                print(f"   ⚠️  No signatures found")
    
    # Medium priority issues
    if medium_priority:
        print(f"\n🟡 MEDIUM PRIORITY ISSUES (Compliance Score 31-70)")
        print("-" * 100)
        for info in medium_priority[:5]:  # Show first 5
            print(f"\n📁 {info['file']}")
            print(f"   Score: {info['compliance_score']}/100")
            if info['has_resigned']:
                print(f"   ⚠️  Contains resigned personnel: {info['all_names']}")
            if info['format_issues']['has_thead']:
                print(f"   ⚠️  Uses vertical signature format")
    
    # Files with correct signatures
    if no_issues:
        print(f"\n✅ FILES WITH CORRECT SIGNATURES")
        print("-" * 100)
        for info in no_issues[:10]:  # Show first 10
            print(f"   ✅ {info['file']}")
        if len(no_issues) > 10:
            print(f"   ... and {len(no_issues) - 10} more")
    
    # Resigned personnel found
    resigned_count = sum(1 for info in results if info['has_resigned'])
    print(f"\n📋 RESIGNED PERSONNEL SIGNATURES FOUND")
    print("-" * 100)
    print(f"Files with resigned signatures: {resigned_count}")
    print("Resigned names that need updating:")
    resigned_names = [
        'Coco Xu (resigned 2025-10-31)', 'ZZ Huang (resigned 2025-01-31)',
        'Nic Weng (resigned 2025-08-31)', 'Alvin Gao (resigned 2025-10-01)',
        'Jimmy Xu (resigned 2025-09-30)', 'Kayla Li (resigned 2024-09-30)',
        'Anya Xiang (resigned 2025-08-31)'
    ]
    for name in resigned_names:
        print(f"   • {name}")
    
    # Format issues
    format_issues_count = sum(1 for info in results if info['format_issues']['has_thead'])
    print(f"\n🔄 FORMAT ISSUES")
    print("-" * 100)
    print(f"Files using vertical format: {format_issues_count}")
    print("These need conversion to horizontal 3-person format")
    
    # Detailed breakdown by name issues
    print(f"\n🔍 DETAILED NAME ANALYSIS")
    print("-" * 100)
    
    # Find specific problematic names
    problematic_patterns = {
        'Rongren Yang': 'Should be: Zen Yang',
        'Zhangyun Gao': 'Should be: ZY Gao (resigned)',
        'Chenjun Weng': 'Should be: Nic Weng (resigned)',
        'Dianjia Zhao': 'Should be: Logan Zhao',
        'Pengtao Gao': 'Should be: Alvin Gao (resigned)',
        'Yanghua Su': 'Should be: YH Su',
        'Gao Zhangyun': 'Should be: ZY Gao (resigned)',
        'Jimmy Xu': 'Should be: PE001 Jimmy Xu (resigned)',
        'Kayla Li': 'Should be: QE001 Kayla Li (resigned)',
        'ZZ Huang': 'Should be: RD004 Coco Xu (resigned)',
        'Nic Weng': 'Should be: RD005 Nic Weng (resigned)',
        'Alvin Gao': 'Should be: RD003 Alvin Gao (resigned)',
        'Zoey Cai': 'Should be: QC002 Zoey Cai',
        'YC Zheng': 'Should be: YC Zheng (DCC Staff)',
        'YC Yang': 'Should be: YC Zheng (typo correction)'
    }
    
    found_issues = {}
    for info in results:
        for name in info['all_names']:
            for pattern, correction in problematic_patterns.items():
                if pattern in name:
                    if pattern not in found_issues:
                        found_issues[pattern] = []
                    found_issues[pattern].append(info['file'])
    
    for pattern, files in found_issues.items():
        print(f"\n🔸 '{pattern}' found in:")
        for file in files:
            print(f"   • {file}")
        print(f"   Correction: {problematic_patterns[pattern]}")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS")
    print("-" * 100)
    print("1. IMMEDIATE ACTIONS:")
    print(f"   - Update {resigned_count} files with resigned personnel signatures")
    print(f"   - Fix {format_issues_count} files with wrong signature format")
    print("   - Replace all Chinese names with English equivalents from TEAM_MEMBERS_REFERENCE.md v3.2")
    
    print("\n2. CORRECTION PRIORITY:")
    print("   High Priority: Chinese names → English names")
    print("   Medium Priority: Resigned personnel → Active personnel")
    print("   Low Priority: Format standardization (vertical → horizontal)")
    
    print("\n3. VERIFICATION CHECKLIST:")
    print("   [ ] All signatures use 3-person horizontal format")
    print("   [ ] No Chinese characters in signatures")
    print("   [ ] All signatories are currently active employees")
    print("   [ ] Correct approval matrix for document type")
    print("   [ ] Consistent name formatting (no '/s/' prefix for active staff)")
    
    print("\n4. REFERENCE MATERIALS:")
    print("   - TEAM_MEMBERS_REFERENCE.md v3.2 (current mappings)")
    print("   - Approval matrix in TEAM_MEMBERS_REFERENCE.md")
    print("   - Signature template in summed-medtech-docs.css")

if __name__ == "__main__":
    main()
