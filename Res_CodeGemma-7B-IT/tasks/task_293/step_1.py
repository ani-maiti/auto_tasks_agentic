import os
import json
from collections import defaultdict

# Find all JSON files in the current directory
json_files = [f for f in os.listdir('.') if f.endswith('.json')]

# Extract unique key paths
key_paths = set()
for file in json_files:
    with open(file) as f:
        data = json.load(f)
        for key in data.keys():
            key_paths.add(key)

# Build a key hierarchy inventory
key_hierarchy = defaultdict(list)
for key in key_paths:
    levels = key.split('.')
    for i in range(len(levels)):
        key_hierarchy[levels[i]].append(key)

# Identify frequently recurring structures
structures = defaultdict(int)
for keys in key_hierarchy.values():
    for i in range(len(keys)):
        structures['.'.join(keys[:i+1])] += 1

# Save inventory to JSON
with open('key_inventory.json', 'w') as f:
    json.dump(key_hierarchy, f)

# Generate report
print('Key Hierarchy Inventory:')
for level, keys in key_hierarchy.items():
    print(f'Level {level}: {keys}')

print('\nFrequently Recurring Structures:')
for structure, count in sorted(structures.items(), key=lambda item: item[1], reverse=True):
    print(f'{structure}: {count}')

# Print most common nested structure
most_common_structure = max(structures, key=structures.get)
print(f'\nMost Common Nested Structure: {most_common_structure}')