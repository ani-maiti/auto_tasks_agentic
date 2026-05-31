import os
from datetime import datetime, timedelta

# Get current time
now = datetime.now()

# Calculate the time 24 hours ago
one_day_ago = now - timedelta(days=1)

# List all files modified within the last 24 hours
modified_files = [f for f in os.listdir('.') if os.path.isfile(f) and datetime.fromtimestamp(os.path.getmtime(f)) > one_day_ago]

# Print the list of modified files
print(modified_files)