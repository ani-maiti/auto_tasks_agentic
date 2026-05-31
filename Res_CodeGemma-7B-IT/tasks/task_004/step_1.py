import os

# Get a list of all files in the current directory
files = os.listdir('.')

# Create a dictionary to store the filenames and their counts
file_counts = {}

# Iterate over the files and count their occurrences
for filename in files:
    if filename in file_counts:
        file_counts[filename] += 1
    else:
        file_counts[filename] = 1

# Print the filenames and their counts
for filename, count in file_counts.items():
    if count > 1:
        print(f"{filename}: {count}")