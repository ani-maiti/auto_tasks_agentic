import os
import re

# Get the list of log files
log_files = [f for f in os.listdir('.') if f.endswith('.log')]

# Create an empty list to store the timeline
timeline = []

# Iterate over the log files
for log_file in log_files:
    # Open the log file
    with open(log_file, 'r') as f:
        # Read the log file line by line
        for line in f:
            # Extract the timestamp and event from each line
            timestamp, event = re.search(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(.*)', line).groups()
            timeline.append((timestamp, event))

# Sort the timeline by timestamp
timeline.sort()

# Create a dictionary to store the activity counts for each hour
activity_counts = {}

# Iterate over the timeline and count the activity for each hour
for timestamp, event in timeline:
    hour = timestamp.split()[1].split(':')[0]
    if hour not in activity_counts:
        activity_counts[hour] = 0
    activity_counts[hour] += 1

# Find the busiest hour
busiest_hour = max(activity_counts, key=activity_counts.get)

# Create a report with the busiest hour and the activity counts
report = f"The busiest hour is {busiest_hour} with {activity_counts[busiest_hour]} events."

# Print the report
print(report)

# Save the timeline to a CSV file
with open('timeline.csv', 'w') as f:
    for timestamp, event in timeline:
        f.write(f"{timestamp},{event}\n")