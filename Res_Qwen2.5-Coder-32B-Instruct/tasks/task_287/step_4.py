import json
from collections import defaultdict

with open('image_metadata.json', 'r') as f:
    image_data = json.load(f)

resolution_groups = defaultdict(list)

for img in image_data:
    resolution = (img['width'], img['height'])
    resolution_groups[resolution].append(img)

grouped_by_resolution = {res: len(images) for res, images in resolution_groups.items()}

with open('resolution_groups.json', 'w') as f:
    json.dump(grouped_by_resolution, f, indent=4)

print("Grouping by resolution complete.")