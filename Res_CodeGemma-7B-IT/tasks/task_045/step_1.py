import glob

# Find all files in the current directory and subdirectories
files = glob.glob("**/*.py", recursive=True)

# Print the list of files
for file in files:
    print(file)