import json
import glob

# Find all JSON files
json_files = glob.glob('*.json')

# Initialize a dictionary to store values and their file names
values_to_files = {}

# Iterate through the JSON files
for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)

    # Iterate through the values in the JSON data
    for value in data.values():
        # Check if the value already exists in the dictionary
        if value in values_to_files:
            # Add the current file name to the list of files for this value
            values_to_files[value].append(file)
        else:
            # Add the value and a list containing the current file name
            values_to_files[value] = [file]

# Create a list of unique values that appear in multiple files
values_in_multiple_files = [value for value, files in values_to_files.items() if len(files) > 1]

# Generate the cross-reference report as Markdown
report = '# Cross-Reference Report\n\n'
for value in values_in_multiple_files:
    report += f'* **Value:** {value}\n'
    report += f'  - Files: {", ".join(values_to_files[value])}\n\n'

# Save the report to a Markdown file
with open('cross_reference_report.md', 'w') as f:
    f.write(report)