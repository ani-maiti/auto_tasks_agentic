import os
import json
from collections import defaultdict

# Get all JSON files in the current directory
json_files = [f for f in os.listdir('.') if f.endswith('.json')]

# Initialize a dictionary to store shared values
shared_values = defaultdict(list)

# Iterate through each JSON file
for file in json_files:
    # Load the JSON data from the file
    with open(file, 'r') as f:
        data = json.load(f)

    # Iterate through the data and extract values
    for key, value in data.items():
        shared_values[value].append(file)

# Remove values that appear only once
shared_values = {k: v for k, v in shared_values.items() if len(v) > 1}

# Create a report of shared values
report = []
for value, files in shared_values.items():
    report.append({
        'value': value,
        'files': files
    })

# Save the report to a JSON file
with open('shared_values.json', 'w') as f:
    json.dump(report, f)

# Print the most frequently shared value
most_common_value, _ = max(shared_values.items(), key=lambda item: len(item[1]))
print(f'Most frequently shared value: {most_common_value}')