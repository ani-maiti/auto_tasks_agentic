# Import the os module
import os

# Check if the file exists
if not os.path.isfile(file):
    print('File not found:', file)
    exit(1)

# Read the file contents
with open(file, 'r') as f:
    contents = f.read()