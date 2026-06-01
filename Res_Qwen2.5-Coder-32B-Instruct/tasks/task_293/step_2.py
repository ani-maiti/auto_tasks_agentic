import json
import os

json_files = [
    "./merged_articles.json",
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

def extract_key_paths(data, parent_key=''):
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}.{k}" if parent_key else k
            yield new_key
            yield from extract_key_paths(v, new_key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]"
            yield from extract_key_paths(item, new_key)

all_keys = set()
for file in json_files:
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            all_keys.update(extract_key_paths(data))
    except Exception as e:
        print(f"Error reading {file}: {e}")

print("Unique key paths found:", len(all_keys))