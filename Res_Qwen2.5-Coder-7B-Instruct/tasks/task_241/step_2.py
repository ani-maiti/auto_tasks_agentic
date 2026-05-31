import os
from collections import defaultdict

image_files = []

# Find all image files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(os.path.join(root, file))

print(f"Found {len(image_files)} image files.")
```

This script will list all image files in the current directory and its subdirectories.