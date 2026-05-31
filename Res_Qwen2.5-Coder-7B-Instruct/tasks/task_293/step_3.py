import json
from collections import defaultdict

key_paths = defaultdict(int)

for file_path in json_files:
    with open(file_path, 'r') as f:
        data = json.load(f)
        def extract_keys(data, parent_key=''):
            if isinstance(data, dict):
                for k, v in data.items():
                    new_key = f"{parent_key}.{k}" if parent_key else k
                    key_paths[new_key] += 1
                    extract_keys(v, new_key)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    extract_keys(item, f"{parent_key}[{i}]")

extract_keys(data)

with open('key_inventory.json', 'w') as f:
    json.dump(key_paths, f, indent=4)

print("Key inventory saved to key_inventory.json")