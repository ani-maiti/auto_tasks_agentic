import os
import time
from datetime import datetime, timedelta

# Get current time
now = datetime.now()

# Calculate 24 hours ago
twenty_four_hours_ago = now - timedelta(hours=24)

# Walk through all files in the directory
for root, dirs, files in os.walk('.'):
    for file in files:
        file_path = os.path.join(root, file)
        # Get modification time
        mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
        # Check if modified within last 24 hours
        if mod_time > twenty_four_hours_ago:
            print(file_path)