import datetime
import os

# Get the current date and time
now = datetime.datetime.now()

# Calculate one week ago
one_week_ago = now - datetime.timedelta(days=7)

# Get a list of files in the current directory
files = os.listdir('.')

# Filter files based on modification time
modified_files = []
for file in files:
    modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(file))
    if modification_time > one_week_ago:
        modified_files.append(file)

# Print the list of modified files
for file in modified_files:
    print(file)