import os

# Define the directory to search
directory = "/path/to/directory"

# Initialize an empty list to store matching files
matching_files = []

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file is a regular file (not a directory)
    if os.path.isfile(os.path.join(directory, filename)):
        # Open the file and read its contents
        with open(os.path.join(directory, filename), "r") as f:
            contents = f.read()

        # Check if the phrase "artificial intelligence" is in the file contents
        if "artificial intelligence" in contents:
            # Add the file name to the list of matching files
            matching_files.append(filename)

# Print the list of matching files
print(matching_files)