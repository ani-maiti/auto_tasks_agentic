import os
import json
from collections import Counter

# Get all files in the current directory tree
files = [f for f in os.walk('.') if f.endswith('.json')]

# Initialize variables
valid_json_files = []
top_level_keys = []

# Iterate over files
for file_path in files:
    # Check if the file is valid JSON
    try:
        with open(file_path, 'r') as f:
            json.load(f)
            valid_json_files.append(file_path)
    except json.JSONDecodeError:
        pass

# Extract top-level keys from valid JSON files
for file_path in valid_json_files:
    with open(file_path, 'r') as f:
        data = json.load(f)
        top_level_keys.extend(data.keys())

# Find the most common keys
key_counts = Counter(top_level_keys)
most_common_keys = key_counts.most_common(10)

# Save analysis to CSV
with open('json_analysis.csv', 'w') as f:
    f.write('File Path,Key,Count\n')
    for file_path, key, count in most_common_keys:
        f.write(f'{file_path},{key},{count}\n')

# Print the ten most common keys
print('Top 10 Most Common Keys:')
for file_path, key, count in most_common_keys:
    print(f'{file_path}: {key} ({count})')