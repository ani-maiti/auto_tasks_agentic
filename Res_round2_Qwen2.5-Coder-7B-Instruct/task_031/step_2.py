import os
from datetime import datetime, timedelta

# Get current date and time
now = datetime.now()

# Calculate the date and time for 7 days ago
seven_days_ago = now - timedelta(days=7)

# List all files in the current directory and its subdirectories
files = []

for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        file_path = os.path.join(root, filename)
        # Check if the file was modified within the last 7 days
        if os.path.getmtime(file_path) > seven_days_ago.timestamp():
            files.append(file_path)

# Print the list of files
print(files)