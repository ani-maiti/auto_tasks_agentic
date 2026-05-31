import os
from datetime import datetime, timedelta

# Get current time
now = datetime.now()

# Calculate the time one hour ago
one_hour_ago = now - timedelta(hours=1)

# List all files in the current directory and its subdirectories
all_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        all_files.append(os.path.join(root, file))

# Filter files modified within the last hour
modified_files = [file for file in all_files if os.path.getmtime(file) > one_hour_ago.timestamp()]

# Print the list of modified files
print(modified_files)