import json
import os
from datetime import datetime
import re

# Function to detect if a string looks like a timestamp
def looks_like_timestamp(s):
    # Common timestamp formats
    patterns = [
        r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?',  # ISO format
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',             # YYYY-MM-DD HH:MM:SS
        r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}',             # MM/DD/YYYY HH:MM:SS
        r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}',             # YYYY/MM/DD HH:MM:SS
        r'\d{4}-\d{2}-\d{2}',                                # YYYY-MM-DD
        r'\d{2}/\d{2}/\d{4}',                                # MM/DD/YYYY
    ]
    
    if isinstance(s, str):
        for pattern in patterns:
            if re.match(pattern, s.strip()):
                return True
    return False

# Function to parse timestamp string to datetime object
def parse_timestamp(ts_str):
    formats = [
        '%Y-%m-%dT%H:%M:%S.%fZ',
        '%Y-%m-%dT%H:%M:%SZ',
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%d %H:%M:%S',
        '%m/%d/%Y %H:%M:%S',
        '%Y/%m/%d %H:%M:%S',
        '%Y-%m-%d',
        '%m/%d/%Y'
    ]
    
    ts_str = ts_str.strip()
    for fmt in formats:
        try:
            return datetime.strptime(ts_str, fmt)
        except ValueError:
            continue
    return None

# Find all JSON files
json_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.json'):
            json_files.append(os.path.join(root, file))

print(f"Found {len(json_files)} JSON files")

# Process each JSON file
all_timestamps = []
timestamp_fields = {}
report_data = []

for file_path in json_files:
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Flatten the JSON structure to find all fields
        def flatten_dict(d, parent_key='', sep='.'):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_dict(v, new_key, sep=sep).items())
                elif isinstance(v, list):
                    # Check if list contains dictionaries
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            items.extend(flatten_dict(item, f"{new_key}.{i}", sep=sep).items())
                        else:
                            items.append((new_key, item))
                else:
                    items.append((new_key, v))
            return dict(items)
        
        flattened = flatten_dict(data)
        
        # Find timestamp-like fields
        timestamp_fields_in_file = []
        file_timestamps = []
        
        for field_name, value in flattened.items():
            if looks_like_timestamp(value):
                parsed_ts = parse_timestamp(value)
                if parsed_ts:
                    timestamp_fields_in_file.append(field_name)
                    file_timestamps.append(parsed_ts)
        
        if file_timestamps:
            min_ts = min(file_timestamps)
            max_ts = max(file_timestamps)
            
            timestamp_fields[file_path] = timestamp_fields_in_file
            report_data.append({
                'file': file_path,
                'timestamp_fields': timestamp_fields_in_file,
                'min_timestamp': min_ts.isoformat(),
                'max_timestamp': max_ts.isoformat(),
                'count': len(file_timestamps)
            })
            
            all_timestamps.extend(file_timestamps)
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Find the oldest timestamp
if all_timestamps:
    oldest_timestamp = min(all_timestamps)
    print(f"Oldest timestamp found: {oldest_timestamp}")
else:
    oldest_timestamp = None
    print("No timestamps found")

# Save report
report = {
    'total_json_files': len(json_files),
    'files_with_timestamps': len(report_data),
    'oldest_timestamp': oldest_timestamp.isoformat() if oldest_timestamp else None,
    'timestamp_ranges': report_data,