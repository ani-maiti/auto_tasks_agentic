import os
from datetime import datetime, timedelta

# Get the current date and time
now = datetime.now()

# Calculate the date and time one day ago
one_day_ago = now - timedelta(days=1)

# Find all files modified within the last day
modified_files = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.getmtime(f) > one_day_ago.timestamp()]

# Print the list of modified files
print(modified_files)