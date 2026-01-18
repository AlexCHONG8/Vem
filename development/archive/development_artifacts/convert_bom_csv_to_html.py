
import csv
import os

def convert_bom_to_html(csv_path, output_path):
    print(f"Reading CSV from: {csv_path}")
    
    rows = []
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        all_lines = list(reader)
        
    # Find the header row (starts with "1,2,3,..." in our analysis of line 9)
    # The user file analysis showed line 9 is the header:
    # 1,2,3,4,5,6,7,8,9,10,Item,名称,Component,Part No.,Tool No.,Quantity,Unit,Rev.,Material,Color,Vendor,Description,,
    
    header_index = -1
    for i, line in enumerate(all_lines):
        if len(line) > 10 and line[10] == "Item" and line[12] == "Component":
            header_index = i
            break
            
    if header_index == -1:
        print("Error: Could not find BOM header row.")
        return

    data_start_index = header_index + 1
    
    # Process data rows
    bom_items = []
    
    for row in all_lines[data_start_index:]:
        if not row or not any(row): # Skip empty rows
            continue
            
        # Determine Level
        level = -1
        # Check first 10 columns for markers like "●" or just non-empty checks if "●" isn't consistent
        # Based on file view: "●" is used.
        for i in range(10):
            if i < len(row) and "●" in row[i]:
                level = i + 1
                break
        
        # If no level marker found, but it has content in Item column, check if it's a valid row
        if level == -1:
            # Maybe it's a footer or metadata
            if len(row) > 10 and row[10]: 
                # fallback logic or skip
                pass
            continue

        # Extract Data
        # Indices based on line 9:
        # 10: Item
        # 12: Component
        # 13: Part No.
        # 14: Tool No.
        # 15: Quantity
        # 16: Unit
        # 17: Rev.
        # 18: Material
        # 19: Color
        # 20: Vendor
        # 21: Description
        
        def get_col(idx):
             return row[idx].strip() if idx < len(row) else ""

        item = {
            "level": level,
            "no": get_col(10),
            "name": get_col(12), # English name
            "part_no": get_col(13),
            "tool_no": get_col(14),
            "qty": get_col(15) + " " + get_col(16),
            "rev": get_col(17),
            "material": translate_material(get_col(18)),
            "color": translate_color(get_col(19)),
            "vendor": translate_vendor(get_col(20)),
            "desc": translate_desc(get_col(21)),
            "chinese_name": get_col(11) # Keep purely for reference if needed, or tooltip
        }
        
        # If English name is missing, use Chinese or placeholder
        if not item["name"] or item["name"] == "-":
             if item["chinese_name"]:
                  # Try to translate common Chinese names if English is missing
                  item["name"] = translate_name(item["chinese_name"])
        
        bom_items.append(item)

    html_content = generate_html(bom_items)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated HTML at: {output_path}")

def translate_color(text):
    translations = {
        "原色": "Natural",
        "透明": "Transparent",
        "白色": "White",
        "黄色": "Yellow",
        "红色": "Red",
        "灰色": "Grey",
        "棕黄": "Brown-Yellow",
        "白/半透明": "White/Translucent"
    }
    for k, v in translations.items():
        if k in text:
            text = text.replace(k, v)
    return text

def translate_material(text):
    # Many are already English or Codes, just ensure cleanliness
    if text == "冷轧不锈钢板": return "Cold Rolled Steel"
    if text == "不锈钢线材": return "Stainless Steel Wire"
    if text == "聚碳酸酯": return "Polycarbonate"
    if text == "热塑性弹性体": return "TPE"
    if text == "聚甲醛": return "POM"
    if text == "聚碳酸酯-丙烯腈共聚物": return "PC+ABS"
    if text == "聚對苯二甲酸乙二酯": return "PET"
    return text

def translate_vendor(text):
    translations = {
        "上海泓辉": "Shanghai Honghui",
        "杜邦": "DuPont",
        "沙伯基础": "SABIC",
        "嘉善豪顺": "Jiashan Haoshun",
        "杭州建林": "Hangzhou Jianlin",
        "昆山传奇": "Kunshan Chuanqi",
        "昆山华一": "Kunshan Huayi",
        "台湾嘉彰": "Taiwan Jiazhang",
        "台湾嘉发": "Taiwan Jiafa"
    }
    for k, v in translations.items():
        if k in text:
            text = text.replace(k, v)
    return text

def translate_desc(text):
    # Handle composite descriptions if needed
    if "箱" in text: text = text.replace("箱", "Carton")
    if "注塑" in text: text = text.replace("注塑", "Injection Molded")
    if "吹塑" in text: text = text.replace("吹塑", "Blow Molded")
    if "半成品和出货包装" in text: text = text.replace("半成品和出货包装", "Semi-finished & Packaging")
    if "组装件" in text: text = text.replace("组装件", "Assembly")
    if "成品" in text: text = text.replace("成品", "Finished Product")
    return text
    
def translate_name(text):
    if text == "总装": return "Final Assembly"
    if text == "前组件+包装": return "Front Subassembly + Packaging"
    if text == "前组件": return "Front Subassembly"
    if text == "垫环": return "Syringe Collar"
    if text == "热塑性弹性体": return "Thermoplastic Elastomer"
    if text == "针筒套筒": return "Syringe Carrier"
    if text == "聚碳酸酯": return "Polycarbonate"
    return text

def generate_html(items):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Bill of Materials (BOM)</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary-color: #2563eb;
            --bg-color: #f8fafc;
            --border-color: #e2e8f0;
            --text-primary: #1e293b;
            --text-secondary: #64748b;
            --row-hover: #f1f5f9;
        }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            margin: 0;
            padding: 20px;
        }}

        .container {{
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 90vh;
        }}

        .controls {{
            padding: 20px;
            border-bottom: 1px solid var(--border-color);
            display: flex;
            gap: 12px;
            align-items: center;
            background: white;
            flex-wrap: wrap;
        }}

        .btn {{
            padding: 8px 16px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: white;
            color: var(--text-secondary);
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }}

        .btn:hover {{
            background: var(--bg-color);
            color: var(--primary-color);
            border-color: var(--primary-color);
        }}

        .btn.active {{
            background: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }}

        .table-container {{
            flex: 1;
            overflow: auto;
            position: relative;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            min-width: 1200px; /* Ensure wide table for attributes */
        }}

        th {{
            background: #f8fafc;
            padding: 12px 16px;
            text-align: left;
            font-weight: 600;
            color: var(--text-secondary);
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            position: sticky;
            top: 0;
            z-index: 10;
            border-bottom: 2px solid var(--border-color);
        }}

        td {{
            padding: 12px 16px;
            border-bottom: 1px solid var(--border-color);
            font-size: 0.9rem;
            vertical-align: middle;
        }}

        tr:hover {{
            background-color: var(--row-hover);
        }}

        /* Column Specifics */
        .col-level {{ width: 60px; text-align: center; }}
        .col-no {{ width: 60px; text-align: center; }}
        .col-name {{ font-weight: 500; min-width: 200px; }}
        .col-part {{ font-family: 'Courier New', monospace; }}
        
        .level-badge {{
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: 600;
        }}
        
        .lvl-1 {{ background: #dbeafe; color: #1e40af; }}
        .lvl-2 {{ background: #ede9fe; color: #5b21b6; }}
        .lvl-3 {{ background: #fce7f3; color: #9d174d; }}
        .lvl-4 {{ background: #dcfce7; color: #166534; }}
        .lvl-5 {{ background: #ffedd5; color: #9a3412; }}

        /* Indentation for Tree View */
        .indent-1 {{ padding-left: 0px; }}
        .indent-2 {{ padding-left: 20px; }}
        .indent-3 {{ padding-left: 40px; }}
        .indent-4 {{ padding-left: 60px; }}
        .indent-5 {{ padding-left: 80px; }}

        .hidden {{
            display: none;
        }}
    </style>
</head>
<body>

<div class="container">
    <div class="controls">
        <span style="font-weight: 600; margin-right: 12px;">View Filter:</span>
        <button class="btn active" onclick="filterLevel('all')">Show All</button>
        <button class="btn" onclick="filterLevel(1)">Final Assy</button>
        <button class="btn" onclick="filterLevel('sub')">Sub-Assemblies</button>
        <button class="btn" onclick="filterLevel(4)">Parts</button>
        <button class="btn" onclick="filterLevel(5)">Materials</button>
    </div>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th class="col-level">Lvl</th>
                    <th class="col-no">No.</th>
                    <th class="col-name">Component Name</th>
                    <th>Part No.</th>
                    <th>Tool No.</th>
                    <th>Qty</th>
                    <th>Rev.</th>
                    <th>Material</th>
                    <th>Color</th>
                    <th>Vendor</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                {generate_table_body(items)}
            </tbody>
        </table>
    </div>
</div>

<script>
    function filterLevel(criteria) {{
        // Update Buttons
        document.querySelectorAll('.btn').forEach(btn => btn.classList.remove('active'));
        event.target.classList.add('active');

        const rows = document.querySelectorAll('tbody tr');
        rows.forEach(row => {{
            const level = parseInt(row.getAttribute('data-level'));
            let show = false;

            if (criteria === 'all') {{
                show = true;
            }} else if (criteria === 'sub') {{
                show = (level === 2 || level === 3);
            }} else {{
                show = (level === criteria);
            }}

            row.className = show ? '' : 'hidden';
        }});
    }}
</script>

</body>
</html>
"""

def generate_table_body(items):
    html = ""
    for item in items:
        # Visual indentation for Name column
        indent_class = f"indent-{item['level']}"
        name_cell = f'<div class="{indent_class}">{item["name"]}</div>'
        
        html += f"""
        <tr data-level="{item['level']}">
            <td class="col-level"><span class="level-badge lvl-{item['level']}">{item['level']}</span></td>
            <td class="col-no">{item['no']}</td>
            <td class="col-name">{name_cell}</td>
            <td class="col-part">{item['part_no']}</td>
            <td>{item['tool_no']}</td>
            <td>{item['qty']}</td>
            <td>{item['rev']}</td>
            <td>{item['material']}</td>
            <td>{item['color']}</td>
            <td>{item['vendor']}</td>
            <td>{item['desc']}</td>
        </tr>
        """
    return html

if __name__ == "__main__":
    csv_file = "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Excel/100-005-BOM-001 BOM 2.0.csv"
    output_html = "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Excel/100-005-BOM-001_Interactive_EN.html"
    
    if os.path.exists(csv_file):
        convert_bom_to_html(csv_file, output_html)
    else:
        print(f"File not found: {csv_file}")
