import os
import zipfile
from pathlib import Path
from collections import defaultdict

# Get the current directory
current_dir = os.getcwd()

# Initialize a dictionary to store file sizes
file_sizes = defaultdict(int)

# Iterate over all files in the current directory
for filename in os.listdir(current_dir):
    # Check if the file is a ZIP archive
    if filename.endswith('.zip'):
        # Open the ZIP archive
        with zipfile.ZipFile(filename, 'r') as zip_file:
            # Iterate over the files in the archive
            for file in zip_file.namelist():
                # Get the file size
                file_size = zip_file.getinfo(file).file_size
                # Add the file size to the dictionary
                file_sizes[filename][file] = file_size

# Find the largest file in each archive
largest_files = {archive: max(files, key=file_sizes[archive].get) for archive, files in file_sizes.items()}

# Print the results to CSV format
print("archive,largest_file")
for archive, file in largest_files.items():
    print(f"{archive},{file}")