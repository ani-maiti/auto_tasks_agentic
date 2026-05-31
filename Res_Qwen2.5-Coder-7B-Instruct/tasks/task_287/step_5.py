# Step 3: Group images by similarity of resolution
resolution_groups = {}
for item in image_data:
    resolution = (item['width'], item['height'])
    if resolution not in resolution_groups:
        resolution_groups[resolution] = []
    resolution_groups[resolution].append(item)

print(f"Grouped {len(resolution_groups)} resolution groups.")