import os

# Get the current working directory
cwd = os.getcwd()

# Get a list of all directories in the current working directory
dirs = [d for d in os.listdir(cwd) if os.path.isdir(os.path.join(cwd, d))]

# Filter directories with more than 50 files
filtered_dirs = [d for d in dirs if len(os.listdir(os.path.join(cwd, d))) > 50]

# Print the list of directories with more than 50 files
print(filtered_dirs)