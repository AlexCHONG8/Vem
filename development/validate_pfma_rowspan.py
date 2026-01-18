#!/usr/bin/env python3
"""
PFMEA Table Rowspan Validator
Detects and reports Item# duplication issues in PFMEA/FMEA tables.

Usage:
    python3 validate_pfma_rowspan.py path/to/document.html

This script checks for:
1. Duplicate Item# numbers (should use rowspan instead)
2. Missing rowspan attributes where they should exist
3. Correct table structure for PFMEA documents
"""

import re
import sys
from pathlib import Path
from collections import defaultdict


def validate_pfma_table(html_file):
    """
    Validate PFMEA table structure and detect rowspan issues.

    Args:
        html_file: Path to HTML file to validate

    Returns:
        dict: Validation results with issues found
    """

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    item_occurrences = defaultdict(list)

    # Find all table rows with Item# numbers
    # Pattern: <td>1</td>, <td>2</td>, etc.
    pattern = r'<td>(\d+)</td>'

    lines = content.split('\n')
    for line_num, line in enumerate(lines, 1):
        # Check if we're in the PFMEA table body section
        if 'class="fmea-table"' in ''.join(lines[max(0, line_num-30):line_num]):
            matches = re.finditer(pattern, line)
            for match in matches:
                item_num = match.group(1)

                # Record line number where this item appears
                item_occurrences[item_num].append(line_num)

                # Check if this line has rowspan
                if 'rowspan=' not in line:
                    # This might be an issue - check context
                    issues.append({
                        'type': 'MISSING_ROWSPAN',
                        'item': item_num,
                        'line': line_num,
                        'context': line.strip()[:100]
                    })

    # Check for consecutive duplicate item numbers
    for item_num, line_numbers in item_occurrences.items():
        if len(line_numbers) > 1:
            # Multiple occurrences of same Item# - likely missing rowspan
            first_line = line_numbers[0]

            # Check if first occurrence has rowspan
            first_line_content = lines[first_line - 1]

            if f'rowspan="{len(line_numbers)}"' not in first_line_content:
                issues.append({
                    'type': 'DUPLICATE_ITEM_NO_ROWSPAN',
                    'item': item_num,
                    'count': len(line_numbers),
                    'first_line': first_line,
                    'lines': line_numbers,
                    'severity': 'HIGH',
                    'recommendation': f'Add rowspan="{len(line_numbers)}" to first occurrence of Item {item_num}'
                })

    # Check for expected items (1-12 for typical PFMEA)
    expected_items = set(range(1, 13))
    found_items = set(int(k) for k in item_occurrences.keys())

    missing_items = expected_items - found_items
    if missing_items:
        issues.append({
            'type': 'MISSING_ITEMS',
            'items': sorted(list(missing_items)),
            'severity': 'MEDIUM'
        })

    return {
        'file': str(html_file),
        'total_issues': len(issues),
        'issues': issues,
        'item_summary': {k: len(v) for k, v in item_occurrences.items()}
    }


def print_validation_report(results):
    """Print detailed validation report."""

    print(f"\n{'='*70}")
    print(f"PFMEA TABLE VALIDATION REPORT")
    print(f"{'='*70}")
    print(f"File: {results['file']}")
    print(f"Total Issues Found: {results['total_issues']}")

    if results['total_issues'] == 0:
        print("\n✅ NO ISSUES DETECTED - Table structure looks good!")
        return

    print(f"\n{'─'*70}")
    print("ISSUE DETAILS:")
    print(f"{'─'*70}")

    for i, issue in enumerate(results['issues'], 1):
        severity = issue.get('severity', 'INFO')

        if issue['type'] == 'DUPLICATE_ITEM_NO_ROWSPAN':
            print(f"\n{i}. {severity}: Item #{issue['item']} appears {issue['count']} times (should use rowspan)")
            print(f"   First occurrence at line: {issue['first_line']}")
            print(f"   All occurrences at lines: {issue['lines']}")
            print(f"   💡 Recommendation: {issue['recommendation']}")

        elif issue['type'] == 'MISSING_ITEMS':
            print(f"\n{i}. {severity}: Missing Items: {issue['items']}")
            print(f"   💡 Recommendation: Verify these items exist in source document")

        elif issue['type'] == 'MISSING_ROWSPAN':
            # Skip individual cell reports to reduce noise
            pass

    print(f"\n{'─'*70}")
    print("ITEM SUMMARY:")
    print(f"{'─'*70}")

    for item in sorted(results['item_summary'].keys()):
        count = results['item_summary'][item]
        print(f"   Item #{item}: {count} occurrence(s)")

    print(f"\n{'='*70}\n")


def generate_fix_commands(results):
    """Generate fix commands for detected issues."""

    if results['total_issues'] == 0:
        return

    print(f"\n{'='*70}")
    print("SUGGESTED FIX COMMANDS")
    print(f"{'='*70}\n")

    for issue in results['issues']:
        if issue['type'] == 'DUPLICATE_ITEM_NO_ROWSPAN':
            item = issue['item']
            rowspan = issue['count']

            print(f"# Fix Item #{item} (appears {rowspan} times)")
            print(f"# 1. Add rowspan to first occurrence:")
            print(f"sed -i '' 's/<td>{item}<\\/td>/<td rowspan=\"{rowspan}\">{item}<\\/td>/' {results['file']}")
            print(f"")
            print(f"# 2. Remove subsequent occurrences:")
            for j, line in enumerate(issue['lines'][1:], 1):
                print(f"# Line {line}: Manually remove <td>{item}</td> and process cell")
            print("")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 validate_pfma_rowspan.py <html_file>")
        print("\nExample:")
        print("  python3 validate_pfma_rowspan.py documents/01-risk-management/100-000-PFA-001_Process_Failure_Mode_Effects_Analysis.html")
        sys.exit(1)

    html_file = Path(sys.argv[1])

    if not html_file.exists():
        print(f"ERROR: File not found: {html_file}")
        sys.exit(1)

    print(f"Validating PFMEA table structure in: {html_file}")

    results = validate_pfma_table(html_file)
    print_validation_report(results)
    generate_fix_commands(results)

    # Exit with error code if issues found
    if results['total_issues'] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
