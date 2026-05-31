import json
from collections import defaultdict

# Read JSON file paths from json_files.txt
with open('json_files.txt', 'r') as f:
    file_paths = f.read().splitlines()

# Dictionary to store values and their corresponding files
value_to_files = defaultdict(list)

# Iterate over each JSON file and extract values
for file_path in file_paths:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            if isinstance(value, str):
                value_to_files[value].append(file_path)

# Filter out values that appear in more than one file
multi_value_files = {key: value for key, value in value_to_files.items() if len(value) > 1}

# Generate Markdown report
report = "# Cross-Reference Report\n\n"
for value, files in multi_value_files.items():
    report += f"- **Value:** `{value}`\n"
    report += "  - **Files:**\n"
    for file in files:
        report += f"    - {file}\n"

# Save report to Markdown file
with open('cross_reference_report.md', 'w') as md_file:
    md_file.write(report)

print("Cross-reference report generated and saved to cross_reference_report.md")