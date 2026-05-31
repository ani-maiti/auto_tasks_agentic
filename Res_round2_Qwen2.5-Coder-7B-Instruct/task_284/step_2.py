import re

# Step 2: Extract headings, tables, links, and code blocks from each Markdown file
content_inventory = []

for file_path in markdown_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Extract headings
        headings = re.findall(r'^(#+)\s+(.*)$', content, re.MULTILINE)
        
        # Extract tables
        tables = re.findall(r'\|.*\|\n\-+\n(.*?)\n', content, re.DOTALL | re.MULTILINE)
        
        # Extract links
        links = re.findall(r'\[([^\]]+)\]\(([^\)]+)\)', content)
        
        # Extract code blocks
        code_blocks = re.findall(r'(```[\s\S]*?```)', content)
        
        content_inventory.append({
            'file_path': file_path,
            'headings': headings,
            'tables': tables,
            'links': links,
            'code_blocks': code_blocks
        })

print("Content inventory created.")