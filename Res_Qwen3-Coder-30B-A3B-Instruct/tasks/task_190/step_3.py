import os
import time
from datetime import datetime, timedelta

# Get current time
now = datetime.now()

# Calculate time one hour ago
one_hour_ago = now - timedelta(hours=1)

# Convert to timestamp
one_hour_ago_timestamp = one_hour_ago.timestamp()

# Walk through directory structure
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            # Get modification time
            mod_time = os.path.getmtime(file_path)
            
            # Check if file was modified within the last hour
            if mod_time >= one_hour_ago_timestamp:
                print(file_path)
        except OSError:
            # Handle files that can't be accessed
            continue