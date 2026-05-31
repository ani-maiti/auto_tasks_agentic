import os
import re

# Set the directory to search
directory = "."

# Create an empty dictionary to store error messages and their counts
error_counts = {}

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a log file
    if filename.endswith(".log"):
        # Open the file and read its contents
        with open(os.path.join(directory, filename), "r") as f:
            # Iterate through each line in the file
            for line in f:
                # Search for error messages in the line
                for error_pattern in ["ERROR", "CRITICAL", "FATAL"]:
                    if error_pattern in line:
                        # Extract the error message from the line
                        error_message = re.search(r": (.*)", line).group(1)
                        # Increment the count for the error message
                        error_counts[error_message] = error_counts.get(error_message, 0) + 1

# Create a list of tuples containing the error message and its count
error_list = list(error_counts.items())

# Sort the list in descending order of count
error_list.sort(key=lambda x: x[1], reverse=True)

# Print the top ten error messages
print("Top 10 Error Messages:")
for error_message, count in error_list[:10]:
    print(f"{error_message}: {count}")