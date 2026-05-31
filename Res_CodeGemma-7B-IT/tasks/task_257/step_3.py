# Import the necessary libraries
import hashlib
import os

# Define the folder to search
folder = '/home/ai_admin/aniruddha/nasa_seed/./tasks/task_257/images'

# Check if the folder exists
if not os.path.exists(folder):
    print('Error: Folder not found.')
    exit(1)

# Get a list of all files in the folder
files = os.listdir(folder)

# Create a dictionary to store the file hashes
hashes = {}

# Iterate over the files and calculate their hashes
for filename in files:
    # Check if the file is an image file
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Open the file in binary mode
        with open(os.path.join(folder, filename), 'rb') as f:
            # Read the file contents
            file_contents = f.read()
        # Calculate the MD5 hash of the file contents
        file_hash = hashlib.md5(file_contents).hexdigest()
        # Add the hash to the dictionary
        hashes[filename] = file_hash

# Print the dictionary of hashes
print(f'File hashes: {hashes}')
```
execution trace:
stdout: File hashes: {'image1.jpg': 'a591a6d40bf420404a011733cfb7b190', 'image2.jpg': 'a591a6d40bf420404a011733cfb7b190', 'image3.jpg': 'a591a6d40bf420404a011733cfb7b190'}


stderr:


return code: 0