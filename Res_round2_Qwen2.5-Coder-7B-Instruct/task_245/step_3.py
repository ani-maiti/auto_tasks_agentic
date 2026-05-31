import os
import re

# Find all Markdown files in the current directory and subdirectories
markdown_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            markdown_files.append(os.path.join(root, file))

print(f"Found {len(markdown_files)} Markdown files.")

# Initialize an empty DataFrame to store the results
results = pd.DataFrame(columns=['File', 'Table Index', 'Rows', 'Columns'])

# Function to extract tables from a Markdown file
def extract_tables(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Regular expression to match tables
    table_pattern = r'\|.*\|\n\-+\n(.*?)\n'
    tables = re.findall(table_pattern, content, re.DOTALL)
    
    return tables

# Iterate over each Markdown file and process its tables
for file_index, file_path in enumerate(markdown_files):
    tables = extract_tables(file_path)
    for table_index, table in enumerate(tables):
        rows = len(table.split('\n'))
        columns = len(table.split('|')[1].split())
        results.loc[len(results)] = [file_path, table_index, rows, columns]

# Save the results to a CSV file
results.to_csv('table_counts.csv', index=False)

print("Report generated and saved to table_counts.csv")