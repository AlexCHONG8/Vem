#!/usr/bin/env python3
"""
Fix PFMEA table rowspan issues in 100-000-PFA-001_Process_Failure_Mode_Effects_Analysis.html

This script adds rowspan attributes to Item# and Process Function columns
based on the failure mode counts from the original Chinese document.
"""

import re
from pathlib import Path

# Define item structures based on Chinese source
item_structures = {
    1: {"rows": 2, "name": "Syringe Barrel & Washer Ring Assembly"},
    2: {"rows": 3, "name": "Syringe Barrel & Needle Cap Assembly"},
    3: {"rows": 2, "name": "Needle Cap and Barrel Assembly"},
    4: {"rows": 2, "name": "Extension Barrel and Barrel Assembly"},
    5: {"rows": 4, "name": "Iron Clip & Cap Press-fit"},
    6: {"rows": 1, "name": "Cap Assembly & Barrel Assembly"},
    7: {"rows": 1, "name": "Actuation Rod & Needle Shield Spring Assembly"},
    8: {"rows": 3, "name": "Actuation Sleeve Assembly"},
    9: {"rows": 5, "name": "Push Rod & Push Rod Spring Installation"},
    10: {"rows": 3, "name": "Rear Cover Installation"},
    11: {"rows": 3, "name": "Tray Loading"},
    12: {"rows": 4, "name": "Final Packaging and Labeling"},
}

def fix_pfmea_table(html_content):
    """
    Fix PFMEA table by adding rowspan attributes to Item# and Process Function columns.

    Args:
        html_content: Original HTML content as string

    Returns:
        Fixed HTML content as string
    """
    lines = html_content.split('\n')
    fixed_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Look for PFMEA table rows (in tbody)
        if '<tr>' in line and 'class="fmea-table' in ''.join(lines[max(0, i-30):i]):
            # Extract the full row (may span multiple lines)
            row_end = i
            while row_end < len(lines) and '</tr>' not in lines[row_end]:
                row_end += 1

            full_row = '\n'.join(lines[i:row_end+1])

            # Check if this is an Item# row (first <td> contains a number 1-12)
            item_match = re.search(r'<td>(\d+)</td>', full_row)

            if item_match:
                item_num = int(item_match.group(1))

                if item_num in item_structures:
                    structure = item_structures[item_num]

                    # Check if this is the FIRST occurrence of this item (needs rowspan)
                    # or a SUBSEQUENT occurrence (should skip Item# and Process Function)

                    # Look back to see if we already added rowspan for this item
                    item_found = False
                    for prev_line in fixed_lines[-50:]:  # Check last 50 lines
                        if f'rowspan="{structure["rows"]}"' in prev_line and f'<td>{item_num}</td>' in prev_line:
                            item_found = True
                            break

                    if not item_found and structure["rows"] > 1:
                        # First occurrence - ADD rowspan
                        # Replace <td>ItemNum</td> with <td rowspan="N">ItemNum</td>
                        fixed_row = full_row.replace(
                            f'<td>{item_num}</td>',
                            f'<td rowspan="{structure["rows"]}">{item_num}</td>',
                            1
                        )

                        # Also add rowspan to Process Function column (second <td>)
                        # Find the process name and wrap it with rowspan
                        process_pattern = r'<td>([^<]+)</td>'
                        process_match = re.search(process_pattern, fixed_row)

                        if process_match:
                            process_name = process_match.group(1)
                            # Only add rowspan if it matches our expected process name
                            if process_name == structure["name"] or process_name.startswith(structure["name"][:20]):
                                fixed_row = fixed_row.replace(
                                    f'<td>{process_name}</td>',
                                    f'<td rowspan="{structure["rows"]}">{process_name}</td>',
                                    1
                                )

                        fixed_lines.append(fixed_row)
                        i = row_end + 1
                        continue
                    elif item_found or structure["rows"] == 1:
                        # Subsequent occurrence - REMOVE Item# and Process Function columns
                        # Split the row into cells and remove first two <td> elements
                        td_pattern = r'<td[^>]*>.*?</td>'
                        cells = re.findall(td_pattern, full_row, re.DOTALL)

                        if len(cells) >= 3:
                            # Remove first two cells (Item# and Process Function)
                            remaining_cells = cells[2:]
                            fixed_row = '                        <tr>\n'

                            for j, cell in enumerate(remaining_cells):
                                fixed_row += f'                            {cell}\n'
                                if j == 0:  # Add proper indentation after first cell
                                    fixed_row += '                        '

                            fixed_row = fixed_row.rstrip() + '\n'
                            fixed_lines.append(fixed_row)
                            i = row_end + 1
                            continue

        fixed_lines.append(line)
        i += 1

    return '\n'.join(fixed_lines)


def main():
    # File path
    html_file = Path("documents/01-risk-management/100-000-PFA-001_Process_Failure_Mode_Effects_Analysis.html")

    if not html_file.exists():
        print(f"ERROR: File not found: {html_file}")
        return

    # Read original file
    print(f"Reading: {html_file}")
    with open(html_file, 'r', encoding='utf-8') as f:
        original_content = f.read()

    # Fix the file
    print("Fixing PFMEA table rowspan attributes...")
    fixed_content = fix_pfmea_table(original_content)

    # Write fixed file
    print(f"Writing: {html_file}")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print("✅ PFMEA table rowspan fix completed!")


if __name__ == "__main__":
    main()
