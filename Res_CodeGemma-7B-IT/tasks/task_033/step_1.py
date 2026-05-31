import os

# Create an empty dictionary to store file sizes as keys and file names as lists of values
file_sizes = {}

# Iterate through all files in the current directory
for filename in os.listdir("."):
    # Get the file size
    file_size = os.path.getsize(filename)

    # Check if the file size is already in the dictionary
    if file_size in file_sizes:
        # If the size exists, add the file name to the list of files for that size
        file_sizes[file_size].append(filename)
    else:
        # If the size doesn't exist, create a new entry in the dictionary with the file size as the key and a list containing the file name
        file_sizes[file_size] = [filename]

# Print the dictionary of file sizes and file names
print(file_sizes)