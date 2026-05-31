import os

# Get a list of files in the current directory
files = os.listdir('.')

# Create a dictionary to store file extensions and counts
extensions = {}

# Iterate over the files and count their extensions
for file in files:
    _, extension = os.path.splitext(file)
    if extension in extensions:
        extensions[extension] += 1
    else:
        extensions[extension] = 1

# Print the report
print('File Extension\tCount')
for extension, count in extensions.items():
    print(f'{extension}\t\t{count}')