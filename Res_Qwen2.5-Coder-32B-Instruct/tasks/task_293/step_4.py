import json
from collections import Counter

def find_most_common_structure(data, parent_key='', structure_counter=Counter()):
    if isinstance(data, dict):
        keys = sorted(data.keys())
        structure = f"{parent_key} -> " + " -> ".join(keys) if parent_key else " -> ".join(keys)
        structure_counter[structure] += 1
        for k, v in data.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            find_most_common_structure(v, new_key, structure_counter)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            find_most_common_structure(item, new_key, structure_counter)
    return structure_counter

most_common_structures = Counter()
for file in json_files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            most_common_structures.update(find_most_common_structure(data))
    except Exception as e:
        print(f"Error reading {file}: {e}")

most_common_structure = most_common_structures.most_common(1)[0]
print("Most common nested structure:", most_common_structure[0])
print("Occurrences:", most_common_structure[1])

with open('key_hierarchy_inventory.json', 'w') as f:
    json.dump(dict(key_inventory), f, indent=4)

with open('most_common_structure_report.txt', 'w') as f:
    f.write(f"Most common nested structure: {most_common_structure[0]}\n")
    f.write(f"Occurrences: {most_common_structure[1]}\n")