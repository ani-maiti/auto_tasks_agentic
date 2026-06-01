import json
import os
from collections import defaultdict

json_files = [
    "./exchange_rates.json",
    "./python_files_sizes.json",
    "./wiki_graph.json",
    "./tasks/task_147/step_1_log.json",
    "./tasks/task_147/step_3_log.json",
    "./tasks/task_147/step_2_log.json",
    "./tasks/task_235/step_1_log.json",
    "./tasks/task_235/step_3_log.json",
    "./tasks/task_235/step_2_log.json"
]

def extract_key_paths(data, parent_key='', key_count=defaultdict(int)):
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            key_count[new_key] += 1
            extract_key_paths(v, new_key, key_count)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            extract_key_paths(item, new_key, key_count)
    return key_count

key_inventory = defaultdict(int)
for file in json_files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            key_inventory.update(extract_key_paths(data))
    except Exception as e:
        print(f"Error reading {file}: {e}")

print("Key inventory built with", len(key_inventory), "unique keys.")