import json
import os
from collections import defaultdict
import statistics

# Initialize data structures to store numeric field values
numeric_fields = defaultdict(list)
field_names = set()

# Find all JSON files in the current directory and subdirectories
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

print(f"Found {len(json_files)} JSON files")

# Process each JSON file
for json_file in json_files:
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Helper function to recursively extract numeric fields
        def extract_numeric_fields(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_path = f"{path}.{key}" if path else key
                    if isinstance(value, (int, float)) and not isinstance(value, bool):
                        numeric_fields[new_path].append(value)
                        field_names.add(new_path)
                    elif isinstance(value, (dict, list)):
                        extract_numeric_fields(value, new_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    new_path = f"{path}[{i}]"
                    if isinstance(item, (int, float)) and not isinstance(item, bool):
                        numeric_fields[new_path].append(item)
                        field_names.add(new_path)
                    elif isinstance(item, (dict, list)):
                        extract_numeric_fields(item, new_path)
        
        extract_numeric_fields(data)
        
    except Exception as e:
        print(f"Error processing {json_file}: {e}")

print(f"Found {len(field_names)} numeric fields across all JSON files")