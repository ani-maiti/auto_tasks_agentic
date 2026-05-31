import os
from collections import defaultdict

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
    # This is a placeholder; you need to implement this part
    resolution = get_image_resolution(file)
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

This script will list all image files, group them by resolution, generate a distribution report, and print the most common resolution. You need to implement the `get_image_resolution` function to get the resolution of an image file.