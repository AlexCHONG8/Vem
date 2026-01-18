
import os
import re
import glob

SOURCE_ROOT = "/Users/alexchong/Desktop/Vem doc/summed-medtech-docs/pharma_audit_templates/Vem audit doc markdown"

def contains_chinese(text):
    return re.search(r'[\u4e00-\u9fff]', text)

def scan_for_chinese():
    html_files = glob.glob(os.path.join(SOURCE_ROOT, "*_EN.html"))
    
    untranslated = set()
    
    print(f"Scanning {len(html_files)} files...")
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Remove HTML tags to process text only
        text_content = re.sub('<[^<]+?>', '', content)
        
        # Split by lines or punctuation to get phrases
        # This is a simple heuristic
        lines = text_content.split('\n')
        for line in lines:
            line = line.strip()
            if contains_chinese(line):
                # Try to extract the specific Chinese part or the whole sentence
                untranslated.add(line)

    print("\n--- Untranslated Phrases ---\n")
    for phrase in sorted(untranslated):
        print(phrase)

if __name__ == "__main__":
    scan_for_chinese()
