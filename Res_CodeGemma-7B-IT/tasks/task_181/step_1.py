import os

# Get a list of all files in the current directory
files = os.listdir(".")

# Create a dictionary to store files by size and name
files_by_size_name = {}

# Iterate over the files and group them by size and name
for filename in files:
    file_path = os.path.join(".", filename)
    file_size = os.path.getsize(file_path)
    files_by_size_name[(file_size, filename)] = files_by_size_name.get((file_size, filename), []) + [file_path]

# Print the files grouped by size and name
for (file_size, filename), file_paths in files_by_size_name.items():
    if len(file_paths) > 1:
        print(f"Duplicate files found:")
        for file_path in file_paths:
            print(f"  {file_path}")