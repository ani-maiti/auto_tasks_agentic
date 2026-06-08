import json
import os

# Get list of JSON files
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

# Check each file for validity
valid_json_files = []
invalid_json_files = []

for file_path in json_files:
    try:
        with open(file_path, 'r') as f:
            json.load(f)
        valid_json_files.append(file_path)
    except json.JSONDecodeError as e:
        invalid_json_files.append((file_path, str(e)))

print("Valid JSON files:")
for file in valid_json_files:
    print(f"  {file}")

print("\nInvalid JSON files:")
for file, error in invalid_json_files:
    print(f"  {file}: {error}")