import json
from collections import defaultdict

key_paths = set()

for json_file in json_files:
    with open(json_file, 'r') as file:
        data = json.load(file)
        def extract_key_paths(data, current_path=''):
            if isinstance(data, dict):
                for key, value in data.items():
                    new_path = f"{current_path}.{key}" if current_path else key
                    key_paths.add(new_path)
                    extract_key_paths(value, new_path)
            elif isinstance(data, list):
                for i, item in enumerate(data):
                    new_path = f"{current_path}[{i}]"
                    extract_key_paths(item, new_path)

extract_key_paths(data)

# Save the key paths to a JSON file
with open('key_paths_inventory.json', 'w') as file:
    json.dump(key_paths, file, indent=4)

print("Key paths extracted and saved to key_paths_inventory.json")