import os

# Get the list of files in the current directory
files = os.listdir('.')

# Extract file extensions
extensions = [os.path.splitext(file)[1] for file in files if os.path.isfile(file)]

# Count unique file extensions
unique_extensions = set(extensions)

print(f"Number of unique file extensions: {len(unique_extensions)}")