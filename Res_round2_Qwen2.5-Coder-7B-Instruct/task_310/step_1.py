import os

# Find all image files in the current directory and its subdirectories
image_files = [f for f in os.walk('.')]  # This will give us a list of tuples (dirpath, dirnames, filenames)
print(image_files)