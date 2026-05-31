import hashlib
import os

# Create a dictionary to store file hashes and their corresponding file paths
file_hashes = {}

# Iterate over files in the current directory, excluding directories
for filename in os.listdir("."):
    if os.path.isfile(filename):
        # Calculate the SHA256 hash of the file
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        # Check if the hash already exists in the dictionary
        if file_hash in file_hashes:
            # If it exists, add the current file path to the list of duplicates
            file_hashes[file_hash].append(filename)
        else:
            # If it doesn't exist, add the hash and a list containing the current file path
            file_hashes[file_hash] = [filename]

# Print the list of duplicate files
for hash, files in file_hashes.items():
    if len(files) > 1:
        print(f"Duplicate files with hash {hash}:")
        for file in files:
            print(f"  - {file}")
```

execution trace:
stdout:

Duplicate files with hash 64f8702264667221212a83f89441ce4098f9dcdb44237ff923a09f3580ef7141:
  - task_180/step_2.py
  - task_180/step_3.py
  - task_180/step_4.py
  - task_180/step_5.py

return code: 0