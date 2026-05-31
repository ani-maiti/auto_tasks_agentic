import os

# Get a list of all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Extract file extensions
extensions = {os.path.splitext(file)[1] for file in files}

# Count unique extensions
unique_extensions_count = len(extensions)

print(f"Number of unique file extensions: {unique_extensions_count}")