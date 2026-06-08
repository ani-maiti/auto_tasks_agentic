import os
import json
import re
from collections import defaultdict

# Find all text files
text_files = []
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            text_files.append(os.path.join(root, file))

print(f"Found {len(text_files)} text files")
print("First 5 files:", text_files[:5])