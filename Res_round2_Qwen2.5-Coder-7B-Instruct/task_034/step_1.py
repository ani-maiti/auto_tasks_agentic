import os

# Define the directory containing the images
image_directory = '/path/to/image/directory'

# List all files in the directory
files = os.listdir(image_directory)

# Initialize a dictionary to store counts by file extension
extension_counts = {}

# Iterate over each file in the directory
for file in files:
    # Split the filename into name and extension
    _, ext = os.path.splitext(file)
    
    # Increment the count for this extension in the dictionary
    if ext in extension_counts:
        extension_counts[ext] += 1
    else:
        extension_counts[ext] = 1

# Print the counts for each extension
print(extension_counts)
```

This script will list all files in the specified directory, count how many files have each extension, and then print the counts. Make sure to replace `/path/to/image/directory` with the actual path to the directory containing your image files.