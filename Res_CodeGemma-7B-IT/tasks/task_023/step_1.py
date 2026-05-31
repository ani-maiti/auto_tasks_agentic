import os

# Get the list of files in the current directory
files = os.listdir(".")

# Create an empty dictionary to store the extension counts
extensions = {}

# Iterate over the files and extract the extensions
for file in files:
    # Get the file extension
    extension = os.path.splitext(file)[1][1:]

    # Increment the count for the extension in the dictionary
    if extension in extensions:
        extensions[extension] += 1
    else:
        extensions[extension] = 1

# Print the extension counts
for extension, count in extensions.items():
    print(f"{extension}: {count}")