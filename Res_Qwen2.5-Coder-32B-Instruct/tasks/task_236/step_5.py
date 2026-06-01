import os
import json
from deepdiff import DeepDiff

print("Identifying files with similar names...")
files = [f for f in os.listdir('.') if f.endswith('.json')]
similar_files = {}

for file in files:
    base_name = '_'.join(file.split('_')[:-1])
    if base_name not in similar_files:
        similar_files[base_name] = []
    similar_files[base_name].append(file)

print("Comparing files with similar names...")
comparison_results = {}

for base_name, file_list in similar_files.items():
    if len(file_list) > 1:
        comparison_results[base_name] = {}
        with open(file_list[0], 'r') as f:
            data1 = json.load(f)
        for other_file in file_list[1:]:
            with open(other_file, 'r') as f:
                data2 = json.load(f)
            diff = DeepDiff(data1, data2)
            comparison_results[base_name][other_file] = diff

print(comparison_results)