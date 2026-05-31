import os
from PIL import Image
from collections import defaultdict

image_files = []
for root, _, files in os.walk('.'):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_files.append(os.path.join(root, file))

resolution_counts = defaultdict(int)

for image_path in image_files:
    with Image.open(image_path) as img:
        width, height = img.size
        resolution_key = f"{width}x{height}"
        resolution_counts[resolution_key] += 1

most_common_resolution = max(resolution_counts.items(), key=lambda x: x[1])
print(f"The most common resolution is {most_common_resolution[0]} with {most_common_resolution[1]} images.")