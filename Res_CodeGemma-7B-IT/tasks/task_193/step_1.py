import os
from datetime import datetime, timedelta

# Calculate the date one month ago
one_month_ago = datetime.now() - timedelta(days=30)

# Iterate over files in the current directory
for filename in os.listdir("."):
    # Get the file's modification time
    modification_time = datetime.fromtimestamp(os.path.getmtime(filename))

    # Check if the file was modified within the last month
    if modification_time > one_month_ago:
        # Print the filename
        print(filename)