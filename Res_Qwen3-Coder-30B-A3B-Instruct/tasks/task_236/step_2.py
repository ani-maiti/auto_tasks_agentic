import json
import os
from pathlib import Path
from difflib import SequenceMatcher
import re

# Find all JSON files
json_files = list(Path('.').rglob('*.json'))
print(f"Found {len(json_files)} JSON files")

# Group files by similar names (using basename without extension)
file_groups = {}
for file_path in json_files:
    base_name = file_path.stem
    # Remove numbers and special characters for grouping
    clean_name = re.sub(r'[\d_]+', '', base_name.lower())
    if clean_name not in file_groups:
        file_groups[clean_name] = []
    file_groups[clean_name].append(file_path)

# Filter groups that have more than one file
similar_groups = {k: v for k, v in file_groups.items() if len(v) > 1}
print(f"Found {len(similar_groups)} groups with similar named files")

# Create HTML report
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>JSON Schema Comparison Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .diff { background-color: #ffebee; }
        .match { background-color: #e8f5e9; }
        .group-title { font-weight: bold; color: #2c5aa0; }
    </style>
</head>
<body>
    <h1>JSON Schema Comparison Report</h1>
"""

# Process each group of similar files
for group_name, files in similar_groups.items():
    html_content += f"<h2 class='group-title'>Group: {group_name}</h2>\n"
    html_content += "<table>\n"
    html_content += "  <tr><th>File</th><th>Schema Elements</th><th>Difference Score</th></tr>\n"
    
    # Load all files in this group
    file_data = []
    for file_path in files:
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                file_data.append((file_path, data))
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue
    
    if len(file_data) < 2:
        html_content += "  <tr><td colspan='3'>Not enough files to compare</td></tr>\n"
        html_content += "</table>\n"
        continue
    
    # Get schema elements from first file as reference
    ref_file, ref_data = file_data[0]
    ref_elements = set()
    def extract_keys(obj, prefix=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_prefix = f"{prefix}.{key}" if prefix else key
                ref_elements.add(new_prefix)
                extract_keys(value, new_prefix)
        elif isinstance(obj, list) and obj:
            # Check first item in list for structure
            extract_keys(obj[0], prefix)
    
    extract_keys(ref_data)
    
    # Compare with other files
    for file_path, data in file_data:
        file_elements = set()
        def extract_keys(obj, prefix=''):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_prefix = f"{prefix}.{key}" if prefix else key
                    file_elements.add(new_prefix)
                    extract_keys(value, new_prefix)
            elif isinstance(obj, list) and obj:
                extract_keys(obj[0], prefix)
        
        extract_keys(data)
        
        # Calculate similarity
        similarity = SequenceMatcher(None, sorted(ref_elements), sorted(file_elements)).ratio()
        diff_count = len(ref_elements.symmetric_difference(file_elements))
        
        html_content += f"  <tr>\n"
        html_content += f"    <td>{file_path.name}</td>\n"
        html_content += f"    <td>{len(file_elements)} elements</td>\n"
        html_content += f"    <td>{similarity:.2%} ({diff_count} differences)</td>\n"
        html_content += "  </tr>\n"
    
    html_content += "</table>\n"

html_content += "</body>\n</html>"

# Save HTML report
with open('json_comparison_report.html', 'w') as f:
    f.write(html_content)

print("Comparison report saved to json_comparison_report.html")