import os
import re

# Step 1: Discover all text files in the current directory and its subdirectories
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

print(f"Found {len(text_files)} text files.")