import os
import json

# Create a list to store file information
files_info = []

# Walk through all directories and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            files_info.append({
                'path': file_path,
                'size': file_size
            })

# Write the information to a JSON file
with open('python_files.json', 'w') as f:
    json.dump(files_info, f, indent=2)

print("JSON file 'python_files.json' has been created.")