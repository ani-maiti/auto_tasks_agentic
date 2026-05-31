#!/usr/bin/env python3

import os
import json
from collections import defaultdict

# Define a function to parse different types of configuration files
def parse_config(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        import yaml
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    elif file_path.endswith('.ini'):
        import configparser
        config = configparser.ConfigParser()
        config.read(file_path)
        return dict(config.items())
    elif file_path.endswith('.toml'):
        import toml
        with open(file_path, 'r') as file:
            return toml.load(file)
    else:
        raise ValueError(f"Unsupported file type: {file_path}")

# Dictionary to store parsed configurations
configurations = defaultdict(dict)

# Iterate over the found configuration files
for file_path in sys.argv[1:]:
    try:
        data = parse_config(file_path)
        # Flatten the dictionary to handle nested structures
        def flatten_dict(d, parent_key='', sep='_'):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
            return dict(items)
        
        flat_data = flatten_dict(data)
        configurations[file_path] = flat_data
    except Exception as e:
        print(f"Error parsing {file_path}: {e}", file=sys.stderr)

# Identify common keys across all configurations
common_keys = set(configurations[next(iter(configurations))].keys())
for _, config in configurations.items():
    common_keys.intersection_update(config.keys())

# Generate a report
report = []
for key in sorted(common_keys):
    values = [str(configs[key]) for configs in configurations.values()]
    report.append([key] + values)

# Save the report to a CSV file
with open('common_keys_report.csv', 'w') as file:
    file.write('\n'.join(','.join(row) for row in report))

print("Report saved to common_keys_report.csv")