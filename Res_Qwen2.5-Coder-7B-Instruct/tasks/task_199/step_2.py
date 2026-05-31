import os
import json
from collections import Counter

# Step 1: Find all JSON files in the current directory tree
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))
print(f"Found {len(json_files)} JSON files.")