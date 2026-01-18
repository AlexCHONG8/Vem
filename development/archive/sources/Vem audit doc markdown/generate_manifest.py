
import os
import re
import json

SOURCE_ROOT = "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit doc markdown"
OUTPUT_FILE = "conversion_manifest.json"

# Manual mapping adjustment based on DHF_Document_Refinement_Review.md and observed files
# Key: Substring in Chinese or English filename -> Value: (Short Form, English Title)
MAPPING = {
    "RMP": ("RMP", "Risk Management Plan"),
    "风险管理计划": ("RMP", "Risk Management Plan"),
    "DFA": ("DFM", "Design Failure Mode and Effects Analysis (DFMEA)"), # DHF Refinement calls it DFM, file says DFA
    "设计失效模式": ("DFM", "Design Failure Mode and Effects Analysis (DFMEA)"),
    "PFA": ("PFM", "Process Failure Mode and Effects Analysis (PFMEA)"), 
    "制程失效模式": ("PFM", "Process Failure Mode and Effects Analysis (PFMEA)"),
    "BOM": ("BOM", "Bill of Materials (BOM)"),
    "PRS": ("PRS", "Product Requirement Specification (PRS)"),
    "产品需求规格": ("PRS", "Product Requirement Specification (PRS)"),
    "URS": ("URS", "User Requirement Specification (URS)"),
    "用户需求": ("URS", "User Requirement Specification (URS)"),
    "BEP": ("BEP", "Biological Evaluation Plan and Report (ISO 10993-1)"),
    "生物相容性": ("BEP", "Biological Evaluation Plan and Report (ISO 10993-1)"),
    "FTP": ("FUN", "Functional Test Plan"), # Functioanl is not strictly in the DHF Refinement table, mapping to closest or generic
    "功能测试": ("VER", "Functional Test Plan"), # Assuming VER or similar. Let's stick to DHF Doc Refinement list if possible. 
                                                # DHF Refinement has "DVM - Test Matrix" or "TIN - Test Instruction". 
                                                # Let's map 'FTP' to 'TIN' (Test Instruction) or create a new one 'FTP' is common. 
                                                # Looking at the file: 100-005-FTP-001 功能测试计划. 
                                                # Let's use 'TVP' (Test Validation Plan) or 'DVP' (Design Verification Plan) if not in list.
                                                # Ref list has "VVM - Product V&V Master Plan".
                                                # Let's use 'FTP' as ShortForm for now to preserve intent if not in list.
    "RTP-001": ("RTP", "Free Fall Test Plan"), # Reliability?
    "自由坠落": ("RTP", "Free Fall Test Plan"),
    "RTP-002": ("RTP", "Transportation Simulation Test Plan"),
    "模拟运输": ("RTP", "Transportation Simulation Test Plan"),
    "STP": ("STP", "Stability Test Plan"), 
    "老化": ("STP", "Stability Test Plan"),
    "IFU": ("IFU", "Instructions for Use (IFU)"),
    "说明书": ("IFU", "Instructions for Use (IFU)"),
    "SIP": ("SIP", "Standard Inspection Procedure (SIP)"), # Refinement differentiates SIP (Comp) and SIP (Assy). Filenames: SIP-001 (Front), SIP-011 (Rear)
    "检验规范": ("SIP", "Standard Inspection Procedure (SIP)"),
}

# Override/refine specific SIPs
SIP_MAPPING = {
    "SIP-001": ("SIC", "Standard Inspection Procedure (SIP) - Front Component"),
    "SIP-011": ("SIC", "Standard Inspection Procedure (SIP) - Rear Cap"),
    "SIP-012": ("SIC", "Standard Inspection Procedure (SIP) - Sleeve"), # Based on file name: 执行套杆
    "SIP-014": ("SIC", "Standard Inspection Procedure (SIP) - Plunger"), # Based on file name: 推杆
}

def scan_files():
    manifest = []
    
    for root, dirs, files in os.walk(SOURCE_ROOT):
        for file in files:
            if not file.endswith(".md") or file == "DHF_Document_Refinement_Review.md" or file == "TEAM_MEMBERS_REFERENCE.md":
                continue
                
            full_path = os.path.join(root, file)
            
            # Parse filename
            # Expected format: 100-005-ZZZ-001 English/Chinese vX.X.md
            match = re.match(r"([\d-]+)-([A-Z]+)-([\d]+)\s*(.*?)(\s*[\d.]*)(_.*)?\.md", file)
            
            doc_number = ""
            short_form = "UNK"
            seq_num = "000"
            english_title = "Unknown Document"
            original_title = file
            version = "1.0"
            
            if match:
                prefix = match.group(1) # 100-005
                file_short_form = match.group(2) # RMP
                seq_num = match.group(3) # 001
                rest = match.group(4) # 自动注射笔...
                
                doc_number = f"{prefix}-{file_short_form}-{seq_num}"
                
                # Determine Mapping
                mapped = None
                
                # Check specifics first
                specific_key = f"{file_short_form}-{seq_num}"
                if specific_key in SIP_MAPPING:
                    mapped = SIP_MAPPING[specific_key]
                else:
                    # Check general
                    if file_short_form in MAPPING:
                        mapped = MAPPING[file_short_form]
                    else:
                        # Fallback search in rest
                        for key, val in MAPPING.items():
                            if key in rest:
                                mapped = val
                                break
                
                if mapped:
                    short_form, english_title = mapped
                    # Ensure ShortForm matches standard. 
                    # If file says DFA but standard says DFM, we use DFM.
                    # The doc number might still be DFA-001 in filename, but we want to display correct Short Form?
                    # Ideally Doc Number reflects Short Form. 
                    # If we change Short Form, we change Doc Number.
                    # e.g. 100-005-DFA-001 -> 100-005-DFM-001.
                    
                    doc_number = f"{prefix}-{short_form}-{seq_num}"
                
                # Extract Version if possible
                v_match = re.search(r"(\d+\.\d+)", file)
                if v_match:
                    version = v_match.group(1)

            else:
                 # Fallback for non-matching files
                 pass

            # Construct Target Filename
            # Format: [Doc Number] [English Title] v[Version]_EN.html
            target_filename = f"{doc_number} {english_title} v{version}_EN.html"
            
            manifest.append({
                "source_path": full_path,
                "original_filename": file,
                "doc_number": doc_number,
                "short_form": short_form,
                "english_title": english_title,
                "target_filename": target_filename,
                "version": version
            })
            
    return manifest

if __name__ == "__main__":
    manifest = scan_files()
    with open(OUTPUT_FILE, "w") as f:
        json.dump(manifest, f, indent=4, ensure_ascii=False)
    print(f"Generated manifest with {len(manifest)} files.")
