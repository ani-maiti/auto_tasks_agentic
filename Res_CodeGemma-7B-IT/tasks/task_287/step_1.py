import os
from PIL import Image
import json

# Get all image files in the current directory
image_files = [f for f in os.listdir('.') if f.endswith(('.jpg', '.jpeg', '.png'))]

# Create a dictionary to store image information
image_info = {}

# Extract image dimensions, formats, and metadata
for image_file in image_files:
    with Image.open(image_file) as img:
        width, height = img.size
        image_info[image_file] = {
            'width': width,
            'height': height,
            'format': img.format,
            'metadata': img.info
        }

# Group images by similarity of resolution
image_groups = {}
for image_file, info in image_info.items():
    key = f"{info['width']}x{info['height']}"
    if key not in image_groups:
        image_groups[key] = []
    image_groups[key].append(image_file)

# Identify duplicate or near duplicate images
duplicates = []
near_duplicates = []
for group in image_groups.values():
    if len(group) > 1:
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                # Calculate similarity based on image dimensions or other metrics
                similarity = calculate_similarity(group[i], group[j])
                if similarity > threshold:
                    near_duplicates.append((group[i], group[j]))
                elif similarity == 1:
                    duplicates.append((group[i], group[j]))

# Save analysis to JSON
with open('image_analysis.json', 'w') as f:
    json.dump(image_info, f)

# Generate report
print("Image Analysis Report")
print("-------------------")
print(f"Total images: {len(image_files)}")
print(f"Duplicate images: {len(duplicates)}")
print(f"Near duplicate images: {len(near_duplicates)}")
print(f"Image groups by resolution: {len(image_groups)}")

# Print largest duplicate group
largest_group = max(image_groups.values(), key=len)
print(f"Largest duplicate group: {len(largest_group)} images")
print(largest_group)