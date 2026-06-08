import os
import re
import csv
from collections import defaultdict, Counter
from pathlib import Path

# Create a list to store all content items
content_inventory = []

# Find all markdown files
markdown_files = list(Path('.').rglob('*.md'))
print(f"Found {len(markdown_files)} markdown files")

# Process each markdown file
for md_file in markdown_files:
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract headings
        headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        headings = [(h[0], h[1].strip()) for h in headings]  # (level, title)
        
        # Extract links
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        
        # Extract code blocks
        code_blocks = re.findall(r'```[\s\S]*?```', content)
        
        # Extract tables (simple approach)
        tables = re.findall(r'(?:\|.*\|\n)*\|.*\|', content)
        
        # Store content items
        file_data = {
            'file': str(md_file),
            'headings': headings,
            'links': links,
            'code_blocks': code_blocks,
            'tables': tables
        }
        
        content_inventory.append(file_data)
        
    except Exception as e:
        print(f"Error processing {md_file}: {e}")

print(f"Processed {len(content_inventory)} files")