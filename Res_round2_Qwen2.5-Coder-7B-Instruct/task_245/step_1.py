import os
import re

# Find all Markdown files in the current directory and subdirectories
markdown_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            markdown_files.append(os.path.join(root, file))

print(f"Found {len(markdown_files)} Markdown files.")