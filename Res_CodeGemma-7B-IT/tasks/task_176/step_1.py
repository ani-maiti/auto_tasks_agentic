import os

# Get all files in the current directory
files = os.listdir('.')

# Create a dictionary to store file extensions and their counts
extensions = {}

# Iterate through files and extract extensions
for file in files:
    _, extension = os.path.splitext(file)
    extensions[extension] = extensions.get(extension, 0) + 1

# Sort extensions by count in descending order
sorted_extensions = sorted(extensions.items(), key=lambda x: x[1], reverse=True)

# Print the report
print("File Extensions:")
for extension, count in sorted_extensions:
    print(f"{extension}: {count}")