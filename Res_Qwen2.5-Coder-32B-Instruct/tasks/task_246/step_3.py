import json
import glob

json_files = glob.glob('**/*.json', recursive=True)
values_dict = {}

def extract_values(data, parent_key=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            if isinstance(value, (str, int, float, bool)):
                if value not in values_dict:
                    values_dict[value] = []
                values_dict[value].append((new_key, file))
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    extract_values(item, f"{new_key}[{index}]")
            else:
                extract_values(value, new_key)

for file in json_files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            extract_values(data)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        continue

cross_reference = {value: files for value, files in values_dict.items() if len(files) > 1}

with open('cross_reference_report.md', 'w') as md_file:
    md_file.write("# Cross-Reference Report\n")
    md_file.write("Values appearing in multiple JSON files:\n\n")
    for value, files in cross_reference.items():
        md_file.write(f"## Value: {value}\n")
        md_file.write("Appears in files:\n")
        for key, file in files:
            md_file.write(f"- {file} (Key: {key})\n")
        md_file.write("\n")

print("Cross-reference report generated.")