import json
import yaml
import toml
import csv
from collections import defaultdict
import os

# Function to parse different config file types
def parse_config_file(file_path):
    try:
        with open(file_path, 'r') as f:
            if file_path.endswith('.json'):
                return json.load(f)
            elif file_path.endswith(('.yaml', '.yml')):
                return yaml.safe_load(f)
            elif file_path.endswith('.ini'):
                # For ini files, we'll just return a simple structure
                return {'content': f.read()}
            elif file_path.endswith('.toml'):
                return toml.load(f)
    except Exception as e:
        print(f"Error parsing {file_path}: {e}")
        return None

# Find all config files
config_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith(('.json', '.yaml', '.yml', '.ini', '.toml')):
            config_files.append(os.path.join(root, file))

print(f"Found {len(config_files)} config files")

# Parse all config files and collect keys
key_counts = defaultdict(int)
all_keys = []

for file_path in config_files:
    parsed_data = parse_config_file(file_path)
    if parsed_data:
        # Flatten the dictionary to get all keys
        def flatten_dict(d, parent_key='', sep='.'):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
            return dict(items)
        
        flattened = flatten_dict(parsed_data)
        keys = list(flattened.keys())
        all_keys.append((file_path, keys))
        
        # Count occurrences of each key
        for key in keys:
            key_counts[key] += 1

# Find keys that appear in more than one file
common_keys = [key for key, count in key_counts.items() if count > 1]

print(f"Found {len(common_keys)} common keys across multiple files")

# Generate report
report_data = []
for file_path, keys in all_keys:
    common_key_values = []
    parsed_data = parse_config_file(file_path)
    
    if parsed_data:
        def get_nested_value(data, key):
            parts = key.split('.')
            current = data
            try:
                for part in parts:
                    current = current[part]
                return current
            except (KeyError, TypeError):
                return None
        
        for key in common_keys:
            value = get_nested_value(parsed_data, key)
            if value is not None:
                # Format value for display
                if isinstance(value, (dict, list)):
                    common_key_values.append(str(value)[:100])  # Truncate long values
                else:
                    common_key_values.append(str(value))
            else:
                common_key_values.append('')
    
    report_data.append([file_path] + common_key_values)

# Save to CSV
with open('config_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    header = ['File Path'] + common_keys
    writer.writerow(header)
    writer.writerows(report_data)

print("Report saved to config_report.csv")