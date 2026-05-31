import os
import json

# Define the directory to scan for Python files
directory = '.'

# Initialize an empty dictionary to store file names and sizes
file_sizes = {}

# Walk through the directory and its subdirectories
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            # Construct the full file path
            file_path = os.path.join(root, file)
            # Get the size of the file
            file_size = os.path.getsize(file_path)
            # Store the file name and size in the dictionary
            file_sizes[file] = file_size

# Convert the dictionary to a JSON string
json_data = json.dumps(file_sizes, indent=4)

# Write the JSON data to a file
with open('python_files_sizes.json', 'w') as f:
    f.write(json_data)

print("JSON file generated successfully.")