import json
from datetime import datetime

timestamps = []

for file in json_files:
    with open(file, 'r') as f:
        data = json.load(f)
        for key, value in data.items():
            if isinstance(value, str) and len(value) >= 19 and value.count('-') == 2 and value.count(':') == 2:
                try:
                    timestamp = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S')
                    timestamps.append(timestamp)
                except ValueError:
                    pass

if timestamps:
    min_timestamp = min(timestamps)
    max_timestamp = max(timestamps)
    print(f"Oldest timestamp: {min_timestamp}")
    print(f"Newest timestamp: {max_timestamp}")
else:
    print("No timestamps found in JSON files.")