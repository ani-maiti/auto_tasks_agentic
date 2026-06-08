import json
import csv
from collections import Counter
import os

# Find all JSON files
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

print(f"Found {len(json_files)} JSON files")

# Validate JSON and extract keys
all_keys = []

for file_path in json_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                all_keys.extend(data.keys())
    except (json.JSONDecodeError, IOError) as e:
        print(f"Skipping invalid JSON file: {file_path}")

print(f"Extracted keys from {len(all_keys)} top-level entries")

# Count key frequencies
key_counts = Counter(all_keys)
print(f"Found {len(key_counts)} unique keys")

# Get top 10 most common keys
top_10 = key_counts.most_common(10)

# Save to CSV
with open('key_analysis.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Key', 'Count'])
    for key, count in key_counts.most_common():
        writer.writerow([key, count])

print("Saved analysis to key_analysis.csv")
print("Top 10 most common keys:")
for key, count in top_10:
    print(f"{key}: {count}")