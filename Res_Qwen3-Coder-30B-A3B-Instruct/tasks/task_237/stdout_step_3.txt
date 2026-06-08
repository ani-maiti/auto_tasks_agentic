import json
import os
from collections import defaultdict

# Initialize data structures
key_counts = defaultdict(int)
file_keys = {}
all_keys = set()

# Process each JSON file
for file_path in os.listdir('.'):
    if file_path.endswith('.json'):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            # Flatten the JSON structure
            flattened_keys = set()
            
            def flatten_dict(d, parent_key='', sep='.'):
                keys = set()
                if isinstance(d, dict):
                    for k, v in d.items():
                        new_key = f"{parent_key}{sep}{k}" if parent_key else k
                        if isinstance(v, dict):
                            keys.update(flatten_dict(v, new_key, sep=sep))
                        elif isinstance(v, list) and v and isinstance(v[0], dict):
                            # Handle list of dictionaries
                            for item in v:
                                if isinstance(item, dict):
                                    keys.update(flatten_dict(item, new_key, sep=sep))
                                else:
                                    keys.add(new_key)
                        else:
                            keys.add(new_key)
                return keys
            
            flattened_keys = flatten_dict(data)
            file_keys[file_path] = flattened_keys
            all_keys.update(flattened_keys)
            
            # Count key frequencies
            for key in flattened_keys:
                key_counts[key] += 1
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

# Save key inventory
with open('key_inventory.txt', 'w') as f:
    for key in sorted(all_keys):
        f.write(f"{key}\n")

# Print keys appearing in more than one file
print("Keys appearing in more than one file:")
for key, count in key_counts.items():
    if count > 1:
        files = [f for f, keys in file_keys.items() if key in keys]
        print(f"  {key}: appears in {count} files ({', '.join(files)})")