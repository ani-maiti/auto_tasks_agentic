import os

# Get the current working directory
cwd = os.getcwd()

# Get a list of files in the current directory tree
files = os.listdir(cwd)

# Filter the files to only include those that are files (not directories)
files = [f for f in files if os.path.isfile(os.path.join(cwd, f))]

# Sort the files by modification time in descending order
files.sort(key=os.path.getmtime, reverse=True)

# Print the ten newest files
for f in files[:10]:
    print(f)