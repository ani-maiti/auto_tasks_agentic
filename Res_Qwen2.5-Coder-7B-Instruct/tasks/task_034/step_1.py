import os

# List of common image file extensions
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}

# Initialize a dictionary to store counts for each image type
image_counts = {ext: 0 for ext in image_extensions}

# Walk through the current directory and its subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        # Check if the file has an image extension
        _, ext = os.path.splitext(file)
        if ext.lower() in image_extensions:
            # Increment the count for this image type
            image_counts[ext] += 1

# Print the results
for ext, count in image_counts.items():
    print(f"{count} {ext} files")
```

This script will walk through the current directory and its subdirectories, counting the number of files with common image extensions (.jpg, .jpeg, .png, .gif, .bmp, .tiff). The results will be printed out showing how many files there are for each image type.