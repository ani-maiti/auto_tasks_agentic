import os
import json

def get_python_files_and_sizes(directory):
    python_files = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                python_files[file_path] = file_size
    return python_files

directory = '.'
python_files = get_python_files_and_sizes(directory)

with open('python_files_sizes.json', 'w') as f:
    json.dump(python_files, f, indent=4)

print("JSON file 'python_files_sizes.json' has been created.")