import datetime
import os

# Get the current time
now = datetime.datetime.now()

# Calculate one hour ago
one_hour_ago = now - datetime.timedelta(hours=1)

# Get the list of files in the current directory
files = os.listdir('.')

# Filter files modified within the last hour
modified_files = []
for file in files:
    file_path = os.path.join('.', file)
    modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
    if modified_time > one_hour_ago:
        modified_files.append(file)

# Print the list of modified files
print(modified_files)