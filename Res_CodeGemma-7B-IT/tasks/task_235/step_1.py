import os
import csv

# Find all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Initialize variables
potential_keys = set()
report = []

# Iterate over CSV files
for file in csv_files:
    with open(file, 'r') as f:
        reader = csv.reader(f)
        first_row = next(reader)

        # Detect potential primary key columns
        for col in first_row:
            if all(row[first_row.index(col)] == row[first_row.index(col)] for row in reader):
                potential_keys.add(col)

    report.append(f'**File:** {file}')
    report.append(f'**Potential primary key columns:** {potential_keys}')

# Generate report
report_text = '\n'.join(report)

# Save report to Markdown file
with open('csv_report.md', 'w') as f:
    f.write(report_text)