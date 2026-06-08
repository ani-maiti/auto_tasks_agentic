import os
import re
import json
from collections import defaultdict, deque

# Find all markdown files
markdown_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            markdown_files.append(os.path.join(root, file))

print(f"Found {len(markdown_files)} markdown files")