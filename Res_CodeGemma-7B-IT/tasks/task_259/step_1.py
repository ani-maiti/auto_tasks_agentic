import os
import re
import datetime
import csv

# Set the directory containing the log files
log_dir = "/path/to/logs"

# Create an empty dictionary to store hourly activity counts
hourly_activity = {}

# Iterate over all files in the log directory
for filename in os.listdir(log_dir):
    # Check if the file is a log file
    if not filename.endswith(".log"):
        continue

    # Open the log file for reading
    with open(os.path.join(log_dir, filename), "r") as f:
        # Read the file line by line
        for line in f:
            # Extract the timestamp from the log line
            timestamp = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
            if timestamp:
                timestamp = datetime.datetime.strptime(timestamp.group(), "%Y-%m-%d %H:%M:%S")

                # Increment the activity count for the corresponding hour
                hour = timestamp.hour
                hourly_activity[hour] = hourly_activity.get(hour, 0) + 1

# Create a CSV file to store the hourly activity data
with open("hourly_activity.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Hour", "Activity Count"])
    for hour, count in hourly_activity.items():
        writer.writerow([hour, count])

# Print the busiest hour
busiest_hour = max(hourly_activity, key=hourly_activity.get)
print("Busiest hour:", busiest_hour)