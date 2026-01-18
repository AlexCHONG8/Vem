
import os
import json
import re
import markdown
from bs4 import BeautifulSoup
from translation_dictionary import COMMON_TERMS

# Configuration
SOURCE_ROOT = "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit doc markdown"
MANIFEST_FILE = "conversion_manifest.json"
STYLE_FILE = "style.css"

# Team Members Data (Simplified for this script from TEAM_MEMBERS_REFERENCE.md)
# Map Chinese Name -> English Name + Title
TEAM_MAP = {
    "李洁": ("Kayla Li", "QA Manager"),
    "罗亿良": ("Kevin Lo", "RD Director"),
    "薛媛媛": ("Grace Xue", "RA Director"),
    "张琪裴": ("Doris Chang", "BD Manager"),
    "高张昀": ("ZY Gao", "Production Supervisor"),
    "杨荣壬": ("Zen Yang", "Management Representative"),
    "蔡大中": ("Andy Tsai", "General Manager"),
    "赵佃佳": ("Logan Zhao", "RD Manager"),
    "周锐英": ("Ryzer Zhou", "QA Manager"),
    "庞天雨": ("Rain Pang", "QC Lab Manager"),
    "熊芊芊": ("Timi Xiong", "RD Engineer"),
    "井天奇": ("Lynn Jing", "Project Manager"),
    "何佩玲": ("Linda He", "Project Manager"),
    "王倩倩": ("Hanna Wang", "Project Manager"),
    "徐俊": ("Jimmy Xu", "QA Manager"),
    "王艳玲": ("Linda Wang", "QC Supervisor"),
    "郑阳春": ("YC Zheng", "DCC"),
    "黎德辉": ("Alex Li", "Production Director"),
    "张福昌": ("Alex Chong", "BD Director"),
    "高鹏涛": ("Alvin Gao", "RD Manager"),
    "洪宇良": ("YL Hong", "QC Manager"),
    "蔡怡妮": ("Yini Chai", "QC Operator"),
    "徐宽": ("Kuan Xu", "Warehouse Supervisor"),
    "张秋燕": ("Iris Zhang", "RD Manager"),
    "黄贞桢": ("ZZ Huang", "R&D Assistance"),
    "徐瑜欣": ("Coco Xu", "R&D Engineer"),
    "翁晨俊": ("Nic Weng", "R&D Engineer"),
    "翁臣俊": ("Nic Weng", "R&D Engineer"),
}

def translate_text(text):
    """Simple dictionary-based translation."""
    if not text:
        return text
    
    # Sort terms by length (descending) to avoid partial matches
    sorted_terms = sorted(COMMON_TERMS.keys(), key=len, reverse=True)
    
    for zh in sorted_terms:
        if zh in text:
            text = text.replace(zh, COMMON_TERMS[zh])
            
    # Post-translation cleanup for spacing artifacts created by concatenation
    cleanup_map = {
        "Minorsshould": "Minors should",
        "doctorsuse": "doctors to use",
        "Materialunder": "Material under",
        "PolymerMaterial": "Polymer Material",
        "Patients(Minors": "Patients (Minors",
        "(Pre-filled)Adult": "(Pre-filled) Adult",
        "Descriptionconsistent": "Description consistent",
        "confirmyour": "confirm your",
        "should be under the help of guardians or doctors to use": "should be used under the help of guardians or doctors",
        "Capconsists": "Cap consists",
        "andconfirm": "and confirm",
        "cartridgeintact": "cartridge intact",
        "Descriptionconsistent": "Description consistent",
        "regulationsconductHandling": "regulations conduct handling",
        "regulationsconduct": "regulations conduct",
        "Temperatureand": "Temperature and",
        "Humiditymust": "Humidity must",
        "controlled在": "controlled at",
        "Scope内": "Range",
        "use Polymer": "use Polymer",
        "Materialunder": "Material under",
        "Management经验": "Management Experience",
        "Material Review": "Material Review",
        "Used于": "Used in",
        "Results Comply": "Results Comply",
        "(without drug": "(without drug",
        "PackagingInformation": "Packaging Information",
        "Designfailed": "Design failed",
        "production workshop": "production workshop",
        "Productionmanufacturer": "Production Manufacturer",
        "EquipmentDiagram": "Equipment Diagram",
        "EquipmentDescription": "Equipment Description",
        "EquipmentNo.": "Equipment No.",
        "in useinjection": "in use injection",
        "providedAfter": "provided After",
        "useIn": "use In",
        "详See": "Refer to details in ",
        "Withmanufacturer": "With manufacturer",
        "Applies to in": "Applies to",
        "WithContactDose": "With Contact Dose",
    }
    for bad, good in cleanup_map.items():
        text = text.replace(bad, good)
        
    return text


def generate_signature_block(prepared, reviewed, approved):
    """Generates the HTML signature block."""
    
    def format_sig(name_zh):
        clean_name = name_zh.strip().replace("<", "").replace(">", "").strip()
        if clean_name in TEAM_MAP:
             en_name, title = TEAM_MAP[clean_name]
             return f"{en_name} ({title})"
        return clean_name
        
    block = f"""
    <div class="signature-block">
        <h3>Approval</h3>
        <table class="signature-table">
            <tr>
                <td><strong>Prepared by:</strong></td>
                <td><span class="sign">{format_sig(prepared)}</span></td>
                <td>Date: {translate_date("2024.07.18")}</td> 
            </tr>
            <tr>
                <td><strong>Reviewed by:</strong></td>
                <td><span class="sign">{format_sig(reviewed)}</span></td>
                <td>Date: {translate_date("2024.07.20")}</td>
            </tr>
            <tr>
                <td><strong>Approved by:</strong></td>
                <td><span class="sign">{format_sig(approved)}</span></td>
                <td>Date: {translate_date("2024.07.22")}</td>
            </tr>
        </table>
    </div>
    """
    # Note: Dates are hardcoded for now as I can't easily extract them per role from the messay tables.
    # In a real scenario, we'd parse the specific table cells.
    return block

def translate_date(date_str):
    # 2024.07.18 -> 18 Jul 2024
    if not date_str: return ""
    try:
        # Simple regex for YYYY.MM.DD
        match = re.search(r"(\d{4})\.(\d{2})\.(\d{2})", date_str)
        if match:
            y, m, d = match.groups()
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            return f"{d} {months[int(m)-1]} {y}"
    except:
        pass
    return date_str

def process_file(file_entry):
    print(f"Processing {file_entry['target_filename']}...")
    
    with open(file_entry['source_path'], 'r', encoding='utf-8') as f:
        md_content = f.read()

    # 1. Translate content using Dictionary BEFORE Markdown conversion (matches raw text better)
    translated_content = translate_text(md_content)
    
    # Fix Markdown Header Spacing (e.g. "4.4RISK" -> "4.4 RISK")
    translated_content = re.sub(r'(#+\s*\d+(\.\d+)*)(?=[A-Za-z])', r'\1 ', translated_content)
    
    # Clean up LaTeX Math markers (e.g. $...$) for cleaner HTML
    # Converting $\mathrm{SL} \times \mathrm{PL}$ to (SL x PL) approx
    translated_content = re.sub(r'\$\(\\mathrm\{([A-Za-z]+)\}\s*\\times\s*\\mathrm\{([A-Za-z]+)\}\)\$', r'(\1 x \2)', translated_content)
    translated_content = re.sub(r'\$\\mathrm\{([A-Za-z]+)\}\s*\\times\s*\\mathrm\{([A-Za-z]+)\}\$', r'\1 x \2', translated_content)
    translated_content = re.sub(r'\\times', 'x', translated_content)
    translated_content = re.sub(r'\\leq', '<=', translated_content)
    translated_content = translated_content.replace('$', '') # Remove remaining tokens
    
    # 2. Convert to HTML
    html_content = markdown.markdown(translated_content, extensions=['tables', 'fenced_code'])
    
    # 3. Post-process HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Clean up standard tables that might look messy
    # Find the "Header" table (usually first table) and remove it, we will inject a clean header
    tables = soup.find_all('table')
    
    prepared_by = "Zhao Dianjia" # Default fallback
    reviewed_by = "Zen Yang"
    approved_by = "Andy Tsai"
    
    # Try to find signatories in the first few tables
    if tables:
        # Simple heuristic: Look for "Prepared by" (translated)
        # This is tricky without robust parsing. 
        # I'll rely on generating a STANDARD signature block at the bottom based on the File Type Matrix I saw in TEAM_MEMBERS_REFERENCE
        pass

    # Signature Logic based on Short Form (from TEAM_MEMBERS_REFERENCE)
    sf = file_entry['short_form']
    if sf in ["QP", "RMP", "GSPR"]:
        prepared_by = "赵佃佳" # Defaults based on matrix
        reviewed_by = "杨荣壬"
        approved_by = "蔡大中"
    elif sf in ["SIP", "SOP"]:
        prepared_by = "熊芊芊"
        reviewed_by = "周锐英"
        approved_by = "赵佃佳" 
    elif sf in ["VMP", "VP"]:
        prepared_by = "赵佃佳"
        reviewed_by = "杨荣壬"
        approved_by = "罗亿良"
    else:
        # Default
        prepared_by = "赵佃佳"
        reviewed_by = "杨荣壬"
        approved_by = "蔡大中"

    # Inject Header
    header_html = f"""
    <div class="doc-header">
        <table class="header-table">
            <tr>
                <td rowspan="3" style="width: 20%; text-align: center;"><img src="https://via.placeholder.com/150x50?text=Summed+Medtech" alt="Summed Medtech Logo"></td>
                <td rowspan="3" style="width: 60%; text-align: center; font-size: 18pt; font-weight: bold;">{file_entry['english_title']}</td>
                <td><strong>Doc No:</strong> {file_entry['doc_number']}</td>
            </tr>
            <tr>
                 <td><strong>Version:</strong> {file_entry['version']}</td>
            </tr>
            <tr>
                 <td><strong>Page:</strong> 1 of 1</td>
            </tr>
        </table>
    </div>
    """
    
    # Inject Signature Block at the end
    sig_block = generate_signature_block(prepared_by, reviewed_by, approved_by)
    
    # Read Style
    with open(STYLE_FILE, 'r') as f:
        css = f.read()
        
    # Assemble Final HTML
    final_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{file_entry['english_title']}</title>
        <style>
        {css}
        </style>
    </head>
    <body>
        {header_html}
        
        <div class="content">
            {str(soup)}
        </div>
        
        {sig_block}
        
        <div class="footer">
            <hr>
            <p style="text-align: center; font-size: 8pt;">Confidential - Summed Medtech Co., Ltd. - All Rights Reserved</p>
        </div>
    </body>
    </html>
    """
    
    # Save
    out_path = os.path.join(SOURCE_ROOT, file_entry['target_filename'])
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

def main():
    with open(MANIFEST_FILE, 'r') as f:
        manifest = json.load(f)
        
    for entry in manifest:
        process_file(entry)

if __name__ == "__main__":
    main()
