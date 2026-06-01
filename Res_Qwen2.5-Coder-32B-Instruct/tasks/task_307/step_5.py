import json
import glob
from collections import defaultdict

json_files = glob.glob('**/*.json', recursive=True)
value_index = defaultdict(set)

def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}_{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}_{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)

for file_path in json_files:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                flat_data = flatten_dict(data)
                for key, value in flat_data.items():
                    value_index[str(value)].add(file_path)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        continue

print(f"Indexed values from {len(json_files)} files.")