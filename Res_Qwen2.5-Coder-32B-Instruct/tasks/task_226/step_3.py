import os
import re
import json
from collections import defaultdict

def extract_code_blocks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return re.findall(r'```(.*?)```', content, re.DOTALL)

def classify_language(code_block):
    lines = code_block.split('\n')
    if len(lines) > 1 and lines[0].strip():
        return lines[0].strip()
    return 'unknown'

def main():
    stats = defaultdict(lambda: {'count': 0, 'blocks': []})
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('.md'):
                md_file_path = os.path.join(root, file)
                code_blocks = extract_code_blocks(md_file_path)
                for block in code_blocks:
                    lang = classify_language(block)
                    stats[lang]['count'] += 1
                    stats[lang]['blocks'].append(block.strip())
    
    with open('code_block_stats.json', 'w') as f:
        json.dump(stats, f, indent=4)

if __name__ == "__main__":
    main()
    print("Code block statistics saved to code_block_stats.json")