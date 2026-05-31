import os
from PIL import Image

image_files = [os.path.join(root, file) for root, _, files in os.walk('.') for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

images_info = []
for img_path in image_files:
    try:
        with Image.open(img_path) as img:
            width, height = img.size
            format = img.format
            mode = img.mode
            images_info.append((img_path, width, height, format, mode))
    except Exception as e:
        print(f"Error processing {img_path}: {e}")

# Save the analysis to JSON
import json
with open('image_analysis.json', 'w') as f:
    json.dump(images_info, f, indent=4)

print("Image analysis saved to image_analysis.json")