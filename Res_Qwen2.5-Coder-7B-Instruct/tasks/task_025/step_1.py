import os
import json

# Get the current working directory
current_directory = os.getcwd()

# List all files and directories in the current directory
files_and_directories = os.listdir(current_directory)

# Initialize an empty dictionary to store file sizes
file_sizes = {}

# Iterate over each item in the directory
for item in files_and_directories:
    # Construct the full path to the item
    full_path = os.path.join(current_directory, item)
    
    # Check if the item is a file
    if os.path.isfile(full_path):
        # Get the size of the file
        file_size = os.path.getsize(full_path)
        
        # Store the file name and size in the dictionary
        file_sizes[item] = file_size

# Convert the dictionary to a JSON string
json_summary = json.dumps(file_sizes, indent=4)

# Print the JSON summary
print(json_summary)