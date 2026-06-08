import json
import os
from collections import defaultdict

# Load all JSON files and extract values
value_to_files = defaultdict(list)
all_values = set()

# Process each JSON file
for json_file in json_files:
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Flatten the JSON structure to get all values
        def extract_values(obj, path=""):
            if isinstance(obj, dict):
                for key, value in obj.items():
                    new_path = f"{path}.{key}" if path else key
                    extract_values(value, new_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    new_path = f"{path}[{i}]"
                    extract_values(item, new_path)
            else:
                # This is a leaf node (string, number, boolean, null)
                value_to_files[str(obj)].append(json_file)
                all_values.add(str(obj))
    except Exception as e:
        print(f"Error processing {json_file}: {e}")

print(f"Extracted {len(all_values)} unique values")
print(f"Found {sum(1 for v in value_to_files.values() if len(v) > 1)} values appearing in multiple files")