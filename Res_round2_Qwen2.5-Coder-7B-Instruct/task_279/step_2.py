import os
import json

# Find all JSON files in the current directory tree
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))
print(json_files)