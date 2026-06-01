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

print(similar_files)