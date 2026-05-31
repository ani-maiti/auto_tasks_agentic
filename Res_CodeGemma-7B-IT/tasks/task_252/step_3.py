import glob
import datetime
import json

# Get a list of all JSON files in the current directory
json_files = glob.glob('*.json')

# Initialize variables to store timestamps and date ranges
timestamps = []
date_ranges = []

# Iterate over each JSON file
for file in json_files:
    # Load the JSON data
    with open(file) as f:
        data = json.load(f)

    # Extract timestamps from the data
    for key, value in data.items():
        if isinstance(value, datetime.datetime):
            timestamps.append(value)

# Sort timestamps in ascending order
timestamps.sort()

# Create a report of the oldest timestamp found
oldest_timestamp = timestamps[0]
report = f"The oldest timestamp found is: {oldest_timestamp}"

# Print the report
print(report)