import os
import re
import csv
from collections import defaultdict

# Find all markdown files
markdown_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            markdown_files.append(os.path.join(root, file))

print(f"Found {len(markdown_files)} markdown files")

# Extract headings from each file
file_headings = defaultdict(list)

for file_path in markdown_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all headings (h1-h6)
        headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        
        # Store headings with their level and file
        for heading_level, heading_text in headings:
            file_headings[heading_text.lower()].append({
                'file': file_path,
                'level': len(heading_level),
                'text': heading_text
            })
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Find duplicated headings
duplicated_headings = {k: v for k, v in file_headings.items() if len(v) > 1}

print(f"Found {len(duplicated_headings)} duplicated headings")

# Generate report
report_data = []
for heading, occurrences in duplicated_headings.items():
    for occurrence in occurrences:
        report_data.append({
            'heading': heading,
            'file': occurrence['file'],
            'level': occurrence['level'],
            'original_text': occurrence['text']
        })

# Save to CSV
with open('duplicated_headings_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['heading', 'file', 'level', 'original_text']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in report_data:
        writer.writerow(row)

print("Report saved to duplicated_headings_report.csv")