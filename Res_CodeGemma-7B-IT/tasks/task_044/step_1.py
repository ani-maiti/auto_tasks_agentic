import os

# Get a list of all files in the current directory
files = os.listdir(".")

# Initialize the smallest file size and name
smallest_file_size = float("inf")
smallest_file_name = None

# Iterate over the files
for file in files:
    # Get the file size
    file_size = os.path.getsize(file)

    # If the file is smaller than the current smallest file, update the smallest file size and name
    if file_size < smallest_file_size:
        smallest_file_size = file_size
        smallest_file_name = file

# Print the smallest file name
print(smallest_file_name)