import json
from collections import defaultdict

json_files = glob.glob('**/*.json', recursive=True)
value_index = defaultdict(set)

for file_path in json_files:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            if isinstance(data, dict):
                for key, value in data.items():
                    value_index[value].add(file_path)
    except (json.JSONDecodeError, FileNotFoundError, PermissionError):
        continue

print(f"Indexed values from {len(json_files)} files.")