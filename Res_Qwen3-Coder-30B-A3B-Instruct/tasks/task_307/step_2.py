import json
import os
from collections import defaultdict, Counter

# Find all JSON files
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

print(f"Found {len(json_files)} JSON files")

# Load all JSON files and extract values
file_values = defaultdict(set)
all_values = defaultdict(list)

for file_path in json_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Flatten the JSON structure to get all values
        def extract_values(obj, path=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    new_path = f"{path}.{k}" if path else k
                    yield from extract_values(v, new_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    new_path = f"{path}[{i}]"
                    yield from extract_values(item, new_path)
            else:
                # This is a leaf value
                yield (path, obj, file_path)
        
        for key_path, value, source_file in extract_values(data):
            # Normalize values for comparison (handle different types)
            normalized_value = str(value)
            file_values[source_file].add(normalized_value)
            all_values[normalized_value].append(source_file)
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Find values that appear in multiple files
shared_values = {value: files for value, files in all_values.items() if len(files) > 1}

# Build cross-reference index
cross_ref_index = {}
for value, files in shared_values.items():
    cross_ref_index[value] = {
        "count": len(files),
        "files": list(set(files))  # Remove duplicates
    }

# Save cross-reference index to JSON
with open('cross_reference_index.json', 'w') as f:
    json.dump(cross_ref_index, f, indent=2)

print(f"Saved cross-reference index with {len(cross_ref_index)} shared values")

# Generate report
report = {
    "total_json_files": len(json_files),
    "total_shared_values": len(cross_ref_index),
    "shared_values_details": cross_ref_index
}

with open('cross_reference_report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Generated cross-reference report")

# Find most frequently shared value
if cross_ref_index:
    most_frequent = max(cross_ref_index.items(), key=lambda x: x[1]['count'])
    print(f"Most frequently shared value: '{most_frequent[0]}' appears in {most_frequent[1]['count']} files")
else:
    print("No shared values found")