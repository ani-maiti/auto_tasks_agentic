import re

def extract_code_blocks(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    code_blocks = re.findall(r'(```[\w\s]*\n([\s\S]*?)\n```)', content)
    return code_blocks

all_code_blocks = []

for file in markdown_files:
    code_blocks = extract_code_blocks(file)
    all_code_blocks.extend(code_blocks)

print(all_code_blocks[:5])  # Print first 5 code blocks for verification