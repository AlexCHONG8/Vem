#!/usr/bin/env python3
"""
Robust fix for PFMEA table rowspan issues.
This version uses more precise matching and handles the multi-line HTML structure better.
"""

import re
from pathlib import Path

# Item structures with rowspan values
ITEMS = {
    1: {"rowspan": 2, "first_line_pattern": r"                        <td>1</td>"},
    2: {"rowspan": 3, "first_line_pattern": r"                        <td>2</td>"},
    3: {"rowspan": 2, "first_line_pattern": r"                        <td>3</td>"},
    4: {"rowspan": 2, "first_line_pattern": r"                        <td>4</td>"},
    5: {"rowspan": 4, "first_line_pattern": r"                        <td>5</td>"},
    6: {"rowspan": 1, "first_line_pattern": r"                        <td>6</td>"},
    7: {"rowspan": 1, "first_line_pattern": r"                        <td>7</td>"},
    8: {"rowspan": 3, "first_line_pattern": r"                        <td>8</td>"},
    9: {"rowspan": 5, "first_line_pattern": r"                        <td>9</td>"},
    10: {"rowspan": 3, "first_line_pattern": r"                        <td>10</td>"},
    11: {"rowspan": 3, "first_line_pattern": r"                        <td>11</td>"},
    12: {"rowspan": 4, "first_line_pattern": r"                        <td>12</td>"},
}

def fix_html_file(filepath):
    """Fix the PFMEA HTML file by adding rowspan attributes."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this line starts a table row with an item number
        item_match = re.match(r'                        <td>(\d+)</td>', line)

        if item_match:
            item_num = int(item_match.group(1))

            if item_num in ITEMS:
                rowspan = ITEMS[item_num]["rowspan"]

                # Check if we already processed this item (look for rowspan in recent output)
                already_fixed = False
                for check_line in result[-100:]:
                    if f'rowspan="{rowspan}"' in check_line and f'<td>{item_num}</td>' in check_line:
                        already_fixed = True
                        break

                if not already_fixed:
                    # This is the FIRST row for this item - ADD rowspan
                    if rowspan > 1:
                        # Modify the item number cell
                        line = line.replace(
                            f'<td>{item_num}</td>',
                            f'<td rowspan="{rowspan}">{item_num}</td>',
                            1
                        )

                        # Look ahead for the process function cell (next line)
                        if i + 1 < len(lines):
                            next_line = lines[i + 1]
                            if '</td>' in next_line and '<td>' in next_line:
                                # Add rowspan to process function cell
                                lines[i + 1] = re.sub(
                                    r'<td>(.+?)</td>',
                                    f'<td rowspan="{rowspan}">\\1</td>',
                                    next_line,
                                    count=1
                                )

                elif rowspan > 1:
                    # This is a SUBSEQUENT row for this item - SKIP first two cells
                    # Find the full row (spanning multiple lines)
                    row_lines = [line]
                    j = i + 1
                    while j < len(lines) and '</tr>' not in lines[j]:
                        row_lines.append(lines[j])
                        j += 1

                    full_row = '\n'.join(row_lines)

                    # Remove first two <td>...</td> cells
                    # Find all <td> tags with their content
                    td_pattern = r'<td[^>]*>.*?</td>'
                    tds = re.findall(td_pattern, full_row, re.DOTALL)

                    if len(tds) >= 3:
                        # Keep all cells except first two
                        remaining_tds = tds[2:]

                        # Reconstruct the row without first two cells
                        new_row = '                        <tr>\n'
                        for k, td in enumerate(remaining_tds):
                            new_row += f'                            {td}\n'

                        new_row = new_row.rstrip() + '\n'
                        result.append(new_row)

                        # Skip the original lines and the look-ahead lines we already captured
                        i = j
                        i += 1
                        continue

        result.append(line)
        i += 1

    # Write result
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(result))

if __name__ == "__main__":
    html_file = Path("documents/01-risk-management/100-000-PFA-001_Process_Failure_Mode_Effects_Analysis.html")

    print(f"Fixing: {html_file}")
    fix_html_file(html_file)
    print("✅ Fix completed!")
