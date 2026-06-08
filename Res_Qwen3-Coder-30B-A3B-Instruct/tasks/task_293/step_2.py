import json
import os
from collections import defaultdict, Counter
from pathlib import Path

# Initialize data structures
all_key_paths = []
key_path_counts = defaultdict(int)
key_hierarchy = defaultdict(set)

def extract_key_paths(obj, parent_path=""):
    """Recursively extract all key paths from a JSON object"""
    if isinstance(obj, dict):
        for key, value in obj.items():
            current_path = f"{parent_path}.{key}" if parent_path else key
            all_key_paths.append(current_path)
            key_path_counts[current_path] += 1
            
            # Track hierarchy
            if parent_path:
                key_hierarchy[parent_path].add(key)
            
            # Continue recursively
            extract_key_paths(value, current_path)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            current_path = f"{parent_path}[{i}]"
            extract_key_paths(item, current_path)

# Process all JSON files
json_files = list(Path(".").rglob("*.json"))
print(f"Found {len(json_files)} JSON files")

for file_path in json_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            extract_key_paths(data)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Build key hierarchy inventory
hierarchy_inventory = {}
for parent, children in key_hierarchy.items():
    hierarchy_inventory[parent] = list(children)

# Find frequently recurring structures
# Group paths by their structure (ignoring indices)
structure_groups = defaultdict(list)
for path in all_key_paths:
    # Remove array indices to group similar structures
    structure = ".".join(part.split("[")[0] for part in path.split("."))
    structure_groups[structure].append(path)

# Find most common nested structures
common_structures = Counter()
for structure, paths in structure_groups.items():
    if len(paths) > 1:  # Only consider structures that appear more than once
        common_structures[structure] = len(paths)

# Save inventory to JSON
inventory_data = {
    "unique_key_paths": sorted(all_key_paths),
    "key_path_frequencies": dict(key_path_counts),
    "key_hierarchy": hierarchy_inventory,
    "common_structures": dict(common_structures)
}

with open('key_hierarchy_inventory.json', 'w') as f:
    json.dump(inventory_data, f, indent=2)

# Generate report
report = {
    "total_json_files": len(json_files),
    "total_unique_key_paths": len(set(all_key_paths)),
    "most_common_structures": common_structures.most_common(10)
}

with open('analysis_report.json', 'w') as f:
    json.dump(report, f, indent=2)

# Print most common nested structure
if common_structures:
    most_common = common_structures.most_common(1)
    print("Most common nested structure:")
    print(most_common[0][0] if most_common else "None")
else:
    print("No recurring structures found")