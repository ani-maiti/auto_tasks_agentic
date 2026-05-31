import os

# Get a list of files in the current directory
files = os.listdir()

# Sort the files by modification time in descending order
files.sort(key=os.path.getmtime, reverse=True)

# Print the 50 most recently modified files
for file in files[:50]:
    print(file)