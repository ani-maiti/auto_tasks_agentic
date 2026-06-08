import re
import csv
from collections import defaultdict
from datetime import datetime
import os

# Find all log files
log_files = []
for root, dirs, files in os.walk('/var/log'):
    for file in files:
        if file.endswith('.log'):
            log_files.append(os.path.join(root, file))

print(f"Found {len(log_files)} log files")

# Extract timestamps and count by hour
hour_counts = defaultdict(int)

# Common timestamp patterns
patterns = [
    r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',  # 2023-01-01 12:30:45
    r'\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}',  # 01/01/2023 12:30:45
    r'\w{3} \d{1,2} \d{2}:\d{2}:\d{2}',      # Jan  1 12:30:45
]

for log_file in log_files[:5]:  # Process first 5 files for testing
    try:
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                for pattern in patterns:
                    matches = re.findall(pattern, line)
                    for match in matches:
                        try:
                            # Try different date formats
                            if '-' in match and ':' in match:
                                dt = datetime.strptime(match, '%Y-%m-%d %H:%M:%S')
                            elif '/' in match and ':' in match:
                                dt = datetime.strptime(match, '%m/%d/%Y %H:%M:%S')
                            else:
                                dt = datetime.strptime(match, '%b %d %H:%M:%S')
                            
                            hour_counts[dt.hour] += 1
                            break  # Found a match, move to next line
                        except ValueError:
                            continue
    except Exception as e:
        print(f"Error processing {log_file}: {e}")

print("Hour counts:", dict(hour_counts))