import json
import os

# Get a list of all files and directories in the current directory
files_and_dirs = [f for f in os.listdir('.') if os.path.isfile(f)]

# Initialize an empty dictionary to store file names and their sizes
file_sizes = {}

# Loop through each file and get its size
for file in files_and_dirs:
    file_path = os.path.join('.', file)
    try:
        size = os.path.getsize(file_path)
        file_sizes[file] = size
    except Exception as e:
        print(f"Error getting size for {file}: {e}")

# Convert the dictionary to a JSON string
json_summary = json.dumps(file_sizes, indent=4)

# Print the JSON summary
print(json_summary)
```

This script will list all files in the current directory, get their sizes, and then output a JSON summary of the files and their sizes. If there are any errors while getting the size of a file, it will print an error message.