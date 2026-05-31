import os
import datetime

# Get the current date and time
now = datetime.datetime.now()

# Calculate the date 7 days ago
seven_days_ago = now - datetime.timedelta(days=7)

# Get a list of all files in the current directory
files = os.listdir()

# Filter files based on modification time
modified_files = [f for f in files if os.path.getmtime(f) >= seven_days_ago.timestamp()]

# Print the list of modified files
for f in modified_files:
    print(f)