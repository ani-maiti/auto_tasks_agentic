import os
import json
from collections import defaultdict
import statistics

# Get all JSON files in the current directory
json_files = [f for f in os.listdir() if f.endswith('.json')]

# Initialize dictionary to store distributions
distributions = defaultdict(list)

# Iterate over JSON files
for file in json_files:
    # Load JSON data
    with open(file, 'r') as f:
        data = json.load(f)

    # Iterate over fields and extract numeric values
    for field in data:
        if isinstance(data[field], (int, float)):
            distributions[field].append(data[field])

# Calculate statistical summaries
summaries = {}
for field, values in distributions.items():
    summaries[field] = {
        'mean': statistics.mean(values),
        'median': statistics.median(values),
        'mode': statistics.mode(values),
        'min': min(values),
        'max': max(values)
    }

# Generate Markdown table
markdown = '| Field | Mean | Median | Mode | Min | Max |\n|---|---|---|---|---|---|'
for field, summary in summaries.items():
    markdown += f'| {field} | {summary["mean"]} | {summary["median"]} | {summary["mode"]} | {summary["min"]} | {summary["max"]} |\n'

# Save Markdown table to file
with open('json_summary.md', 'w') as f:
    f.write(markdown)
```
execution trace:
stdout:


stderr:
Traceback (most recent call last):
  File "/home/ai_admin/aniruddha/nasa_seed/./tasks/task_268/step_2.py", line 20, in <module>
    if isinstance(data[field], (int, float)):
TypeError: list indices must be integers or slices, not dict


return code: 1