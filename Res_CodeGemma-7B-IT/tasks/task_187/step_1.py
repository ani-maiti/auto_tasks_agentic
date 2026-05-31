import os

# Get the current directory
cwd = os.getcwd()

# List all files in the directory
files = os.listdir(cwd)

# Filter files for executable files
executables = [f for f in files if os.access(f, os.X_OK)]

# Print the size of each executable file
for f in executables:
    size = os.path.getsize(f)
    print(f"{f}: {size}")