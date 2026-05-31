import os

# Get the current working directory
cwd = os.getcwd()

# Create an empty dictionary to store the file extensions and their counts
extensions = {}

# Iterate over all files in the current directory and subdirectories
for filename in os.walk(cwd):
    # Get the extension of each file
    file_ext = os.path.splitext(filename)[-1]

    # Increment the count for the file extension in the dictionary
    extensions[file_ext] = extensions.get(file_ext, 0) + 1

# Find the extension with the highest count
most_common_ext = max(extensions, key=extensions.get)

# Print the most common extension
print(f"Most common extension: {most_common_ext}")