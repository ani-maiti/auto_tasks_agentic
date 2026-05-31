import os

# Get the current directory
directory = os.getcwd()

# Initialize a dictionary to store the file counts by extension
file_counts = {}

# Iterate over the files in the directory
for filename in os.listdir(directory):
    # Get the file extension
    file_extension = os.path.splitext(filename)[1]

    # Increment the count for the extension
    if file_extension in file_counts:
        file_counts[file_extension] += 1
    else:
        file_counts[file_extension] = 1

# Print the file counts by extension
for extension, count in file_counts.items():
    print(f"{extension}: {count}")