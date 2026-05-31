import os
from collections import defaultdict
from PIL import Image

image_files = []

# Find all image files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_files.append(os.path.join(root, file))

print(f"Found {len(image_files)} image files.")

# Group images by resolution
resolution_dict = defaultdict(list)

for file in image_files:
    # Get the resolution of the image
    with Image.open(file) as img:
        resolution = img.size
        resolution_dict[resolution].append(file)

print("Image files grouped by resolution:")
for resolution, files in resolution_dict.items():
    print(f"{resolution}: {len(files)} files")

# Generate distribution report
report = "Distribution Report:\n"
for resolution, files in resolution_dict.items():
    report += f"{resolution}: {len(files)} files\n"

print(report)

# Print the most common resolution
most_common_resolution = max(resolution_dict, key=resolution_dict.get)
print(f"The most common resolution is: {most_common_resolution}")
```

This script will list all image files, group them by resolution, generate a distribution report, and print the most common resolution. The `get_image_resolution` function uses the Python Imaging Library (PIL) to get the resolution of an image file. Make sure you have PIL installed (`pip install pillow`).