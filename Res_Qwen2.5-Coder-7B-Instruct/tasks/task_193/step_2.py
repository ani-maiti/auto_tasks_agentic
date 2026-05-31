import os
from datetime import datetime, timedelta

# Get current date and subtract one month
one_month_ago = datetime.now() - timedelta(days=30)

# List all files in the current directory and its subdirectories
all_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        all_files.append(os.path.join(root, file))

# Filter files modified within the last month
modified_files = [f for f in all_files if os.path.getmtime(f) > one_month_ago.timestamp()]

# Print the list of modified files
print(modified_files)