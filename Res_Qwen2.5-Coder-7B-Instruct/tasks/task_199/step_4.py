# Step 2: Determine which JSON files are valid
valid_json_files = []
invalid_json_files = []

for json_file in json_files:
    try:
        with open(json_file, 'r') as f:
            json.load(f)
        valid_json_files.append(json_file)
    except json.JSONDecodeError:
        invalid_json_files.append(json_file)

print(f"Valid JSON files: {len(valid_json_files)}")
print(f"Invalid JSON files: {len(invalid_json_files)}")