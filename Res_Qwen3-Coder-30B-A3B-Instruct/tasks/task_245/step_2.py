import re
import csv
from pathlib import Path

# Function to extract tables from markdown content
def extract_tables(markdown_content):
    # Find all table patterns
    table_pattern = r'\|.*\|\n\|.*\|\n(?:\|.*\|\n)*'
    tables = re.findall(table_pattern, markdown_content, re.MULTILINE)
    return tables

# Function to count rows and columns in a table
def count_table_dimensions(table_str):
    lines = table_str.strip().split('\n')
    if len(lines) < 2:
        return 0, 0
    
    # Count columns from the first line (header)
    columns = len(lines[0].split('|')) - 1  # Subtract 1 for the leading/trailing pipe
    
    # Count rows (excluding header)
    rows = len(lines) - 1
    
    return rows, columns

# Find all markdown files
markdown_files = list(Path('.').rglob('*.md'))

# Prepare CSV data
csv_data = []
csv_data.append(['File', 'Table Number', 'Rows', 'Columns'])

# Process each markdown file
for file_path in markdown_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tables = extract_tables(content)
        
        for i, table in enumerate(tables):
            rows, columns = count_table_dimensions(table)
            csv_data.append([str(file_path), str(i+1), str(rows), str(columns)])
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Write to CSV file
with open('table_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csv_data)

print("Report generated successfully.")