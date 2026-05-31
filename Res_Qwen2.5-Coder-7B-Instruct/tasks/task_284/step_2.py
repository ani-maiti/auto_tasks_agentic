import re
from collections import defaultdict

markdown_files = ['./consolidation_report.md', './command_frequency.md', './cross_reference_report.md']

content_inventory = defaultdict(list)

for file_path in markdown_files:
    with open(file_path, 'r') as file:
        content = file.read()
        
        # Extract headings
        headings = re.findall(r'^(#+)\s+(.*)$', content, re.MULTILINE)
        for level, heading in headings:
            content_inventory['headings'].append((file_path, level, heading))
            
        # Extract tables
        tables = re.findall(r'\|.*\|\n\-+\n(.*?)\n', content, re.DOTALL)
        for table in tables:
            content_inventory['tables'].append((file_path, table.strip()))
            
        # Extract links
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        for link_text, link_url in links:
            content_inventory['links'].append((file_path, link_text, link_url))
            
        # Extract code blocks
        code_blocks = re.findall(r'(```[\w\s]*\n)(.*?)(```)', content, re.DOTALL)
        for code_block in code_blocks:
            content_inventory['code_blocks'].append((file_path, code_block[1].strip()))

print(content_inventory)