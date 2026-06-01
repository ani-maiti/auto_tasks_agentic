import os
from PIL import Image
import json

image_files = [line.strip() for line in open('image_files.txt', 'r')]

image_data = []

for file_path in image_files:
    try:
        with Image.open(file_path) as img:
            width, height = img.size
            format = img.format
            mode = img.mode
            info = img.info
            image_data.append({
                'file_path': file_path,
                'width': width,
                'height': height,
                'format': format,
                'mode': mode,
                'info': info
            })
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

with open('image_metadata.json', 'w') as f:
    json.dump(image_data, f, indent=4)

print("Metadata extraction complete.")