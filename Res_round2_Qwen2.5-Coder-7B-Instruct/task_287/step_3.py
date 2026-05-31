import json

# Load the image analysis data
with open('image_analysis.json', 'r') as f:
    images_info = json.load(f)

# Group images by resolution
resolution_groups = {}
for img_info in images_info:
    resolution = (img_info[1], img_info[2])
    if resolution not in resolution_groups:
        resolution_groups[resolution] = []
    resolution_groups[resolution].append(img_info[0])

# Identify duplicate or near duplicate images
duplicate_groups = []
tolerance = 10  # Allow up to 10 pixels difference in resolution
for resolution, paths in resolution_groups.items():
    if len(paths) > 1:
        for i in range(len(paths)):
            for j in range(i + 1, len(paths)):
                path1 = paths[i]
                path2 = paths[j]
                with Image.open(path1) as img1, Image.open(path2) as img2:
                    diff = sum(abs(x - y) for x, y in zip(img1.getdata(), img2.getdata()))
                    if diff < tolerance * img1.width * img1.height:
                        duplicate_groups.append((path1, path2))

# Save the analysis to JSON
with open('duplicates_analysis.json', 'w') as f:
    json.dump(duplicate_groups, f, indent=4)

print("Duplicate analysis saved to duplicates_analysis.json")