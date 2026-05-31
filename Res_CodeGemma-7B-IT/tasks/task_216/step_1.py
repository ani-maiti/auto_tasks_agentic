import os
import json
from collections import Counter

def flatten_json(json_data):
    flattened = []
    for key, value in json_data.items():
        if isinstance(value, dict):
            flattened.extend(flatten_json(value).items())
        else:
            flattened.append((key, value))
    return flattened

def count_keys(json_files):
    key_counts = Counter()
    for file in json_files:
        with open(file, 'r') as f:
            data = json.load(f)
            flattened_data = flatten_json(data)
            key_counts.update(key for key, _ in flattened_data)
    return key_counts

def save_key_inventory(key_counts, output_file):
    with open(output_file, 'w') as f:
        for key, count in key_counts.most_common():
            f.write(f"{key}: {count}\n")

def find_keys_in_multiple_files(json_files):
    key_counts = count_keys(json_files)
    keys_in_multiple_files = [key for key, count in key_counts.items() if count > 1]
    return keys_in_multiple_files

json_files = [f for f in os.listdir('.') if f.endswith('.json')]
key_counts = count_keys(json_files)
save_key_inventory(key_counts, 'key_inventory.txt')
keys_in_multiple_files = find_keys_in_multiple_files(json_files)
print(f"Keys appearing in multiple files: {keys_in_multiple_files}")