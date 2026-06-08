import os
import time
from datetime import datetime, timedelta

# Calculate the timestamp for 7 days ago
seven_days_ago = datetime.now() - timedelta(days=7)
seven_days_ago_timestamp = seven_days_ago.timestamp()

# Find all files modified within the last 7 days
files_modified_recently = []
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            # Get the modification time of the file
            mod_time = os.path.getmtime(file_path)
            
            # Check if the file was modified within the last 7 days
            if mod_time >= seven_days_ago_timestamp:
                files_modified_recently.append(file_path)
        except (OSError, IOError):
            # Skip files that can't be accessed
            continue

# Print the list of files
for file in files_modified_recently:
    print(file)