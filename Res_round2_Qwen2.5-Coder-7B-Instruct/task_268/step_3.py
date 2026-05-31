# Ensure all file paths exist before attempting to load them
import os

for file_path in file_paths:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        file_paths.remove(file_path)

data = load_json_files(file_paths)