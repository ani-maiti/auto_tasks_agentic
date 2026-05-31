import os

# Get the current directory
current_dir = os.getcwd()

# Set the search term
search_term = "data science"

# Iterate over files in the current directory
for filename in os.listdir(current_dir):
    # Check if the file is a file (not a directory)
    if os.path.isfile(filename):
        # Check if the file contains the search term
        if search_term in open(filename).read():
            # Print the filename
            print(filename)