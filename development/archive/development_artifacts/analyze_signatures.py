#!/usr/bin/env python3
import os
import re
import json
from pathlib import Path

def extract_signatures_from_html(file_path):
    """Extract signature blocks from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all signature blocks
        signature_pattern = r'<div class="signature-name[^"]*">([^<]+)</div>\s*<div class="signature-title">([^<]+)</div>\s*<div class="signature-label">([^<]+)</div>'
        matches = re.findall(signature_pattern, content, re.DOTALL)
        
        signatures = []
        for name, title, role in matches:
            signatures.append({
                'name': name.strip(),
                'title': title.strip(),
                'role': role.strip()
            })
        
        return signatures
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def has_chinese_names(signatures):
    """Check if any signature contains Chinese characters"""
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    for sig in signatures:
        if chinese_pattern.search(sig['name']):
            return True
    return False

def has_incorrect_format(file_path):
    """Check if file uses vertical format (with thead) instead of horizontal"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return 'thead' in content and 'signature-table' in content
    except:
        return False

# Load team members reference
def load_team_members():
    team_members = {}
    
    # Active members mapping
    active_members = {
        '蔡大中': ('Andy Tsai', 'General Manager'),
        '杨荣壬': ('Zen Yang', 'ISO13485 Management Representative'),
        '周锐英': ('Ryzer Zhou', 'QA Manager'),
        '庞天雨': ('Rain Pang', 'QC Lab Manager'),
        '蔡怡妮': ('Zoey Cai', 'QC Operator'),
        '薛媛媛': ('Grace Xue', 'RA Director'),
        '黎德辉': ('Alex Li', 'Production Director'),
        '罗亿良': ('Kevin Lo', 'RD Director'),
        '张福昌': ('Alex Chong', 'BD Director'),
        '赵佃佳': ('Logan Zhao', 'RD Manager'),
        '张琪裴': ('Doris Chang', 'BD Manager'),
        '熊芊芊': ('Timi Xiong', 'RD Engineer'),
        '苏杨华': ('YH Su', 'Production Operator'),
        '井天奇': ('Lynn Jing', 'Project Manager'),
        '何佩玲': ('Linda He', 'Project Manager'),
        '王倩倩': ('Hanna Wang', 'Project Manager'),
        '徐宽': ('Kuan Xu', 'Supervisor'),
        '郑阳春': ('YC Zheng', 'DCC Staff'),
        '王艳玲': ('Linda Wang', 'QC Supervisor')
    }
    
    for chinese_name, (english_name, title) in active_members.items():
        team_members[chinese_name] = english_name
    
    return team_members

def main():
    documents_dir = Path("documents")
    html_files = list(documents_dir.glob("*.html")) + list(documents_dir.rglob("*.html"))
    
    print(f"Found {len(html_files)} HTML files\n")
    
    team_members = load_team_members()
    results = {
        'total_files': len(html_files),
        'correct_signatures': [],
        'need_correction': [],
        'missing_signatures': [],
        'wrong_format': [],
        'issues': []
    }
    
    for html_file in sorted(html_files):
        signatures = extract_signatures_from_html(html_file)
        relative_path = html_file.relative_to(Path.cwd())
        
        if not signatures:
            results['missing_signatures'].append(str(relative_path))
            continue
            
        has_chinese = has_chinese_names(signatures)
        wrong_format = has_incorrect_format(str(html_file))
        
        if has_chinese:
            # Find which Chinese names need correction
            corrections = []
            for sig in signatures:
                for chinese_name, english_name in team_members.items():
                    if chinese_name in sig['name']:
                        corrections.append({
                            'chinese': chinese_name,
                            'english': english_name,
                            'current': sig['name']
                        })
            
            results['need_correction'].append({
                'file': str(relative_path),
                'corrections': corrections,
                'format_issue': wrong_format
            })
        elif wrong_format:
            results['wrong_format'].append(str(relative_path))
        else:
            results['correct_signatures'].append(str(relative_path))
    
    # Print summary
    print("=" * 80)
    print("SIGNATURE VERIFICATION SUMMARY")
    print("=" * 80)
    print(f"Total HTML files: {results['total_files']}")
    print(f"Files with correct signatures: {len(results['correct_signatures'])}")
    print(f"Files needing Chinese name corrections: {len(results['need_correction'])}")
    print(f"Files with wrong signature format: {len(results['wrong_format'])}")
    print(f"Files missing signatures: {len(results['missing_signatures'])}")
    print()
    
    # Detailed breakdown
    if results['need_correction']:
        print("� FILES NEEDING CHINESE NAME CORRECTIONS:")
        print("-" * 80)
        for item in results['need_correction']:
            print(f"\n📁 {item['file']}")
            if item['format_issue']:
                print("   ⚠️  ALSO uses vertical signature format (needs conversion)")
            for correction in item['corrections']:
                print(f"   🔸 {correction['chinese']} → {correction['english']}")
                print(f"      Current: '{correction['current']}'")
    
    if results['wrong_format']:
        print("\n📁 FILES WITH WRONG SIGNATURE FORMAT (Vertical instead of Horizontal):")
        print("-" * 80)
        for file_path in results['wrong_format']:
            print(f"   📄 {file_path}")
    
    if results['missing_signatures']:
        print("\n📁 FILES MISSING SIGNATURES:")
        print("-" * 80)
        for file_path in results['missing_signatures']:
            print(f"   📄 {file_path}")
    
    # Print by category
    print("\n" + "=" * 80)
    print("BREAKDOWN BY DOCUMENT CATEGORY")
    print("=" * 80)
    
    categories = {
        '01-risk-management': [],
        '02-design-input': [],
        '03-design-verification': [],
        '04-design-output': [],
        '07-materials-components': [],
        'other': []
    }
    
    for file_path in results['correct_signatures']:
        category = 'other'
        if '01-risk-management' in file_path:
            category = '01-risk-management'
        elif '02-design-input' in file_path:
            category = '02-design-input'
        elif '03-design-verification' in file_path:
            category = '03-design-verification'
        elif '04-design-output' in file_path:
            category = '04-design-output'
        elif '07-materials-components' in file_path:
            category = '07-materials-components'
        
        categories[category].append(file_path)
    
    for category, files in categories.items():
        if files:
            print(f"\n✅ {category.replace('-', ' ').title()}: {len(files)} files")
            for file_path in files[:3]:  # Show first 3
                print(f"   📄 {os.path.basename(file_path)}")
            if len(files) > 3:
                print(f"   ... and {len(files) - 3} more")
    
    print("\n" + "=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print("1. PRIORITY - Fix Chinese names in signature blocks")
    if results['need_correction']:
        print(f"   - {len(results['need_correction'])} files need name corrections")
        print("   - Use TEAM_MEMBERS_REFERENCE.md v3.2 for correct mappings")
    
    print("\n2. FORMAT - Convert vertical to horizontal signature format")
    if results['wrong_format']:
        print(f"   - {len(results['wrong_format'])} files need format conversion")
        print("   - Remove <thead>, use single <tr> with 3 <td> elements")
    
    print("\n3. COMPLETION - Add missing signatures")
    if results['missing_signatures']:
        print(f"   - {len(results['missing_signatures'])} files have no signatures")
    
    print("\n4. VERIFICATION - Review corrected files")
    print("   - Check that all signatures follow the 3-person horizontal format")
    print("   - Verify no Chinese characters remain in signatures")
    print("   - Ensure proper approval matrix for document types")

if __name__ == "__main__":
    main()
