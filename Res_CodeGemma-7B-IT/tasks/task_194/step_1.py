import datetime

# Get the current date and time
now = datetime.datetime.now()

# Calculate the date one day ago
one_day_ago = now - datetime.timedelta(days=1)

# List all files accessed within the last day
files_accessed_today = []
for filename in os.listdir("."):
    file_accessed_time = datetime.datetime.fromtimestamp(os.path.getatime(filename))
    if file_accessed_time >= one_day_ago:
        files_accessed_today.append(filename)

# Print the list of files accessed today
print(files_accessed_today)