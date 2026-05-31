import os
from PIL import Image

image_path = './histogram.png'
try:
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data:
            print(f"Metadata for {image_path}:")
            for tag_id, value in exif_data.items():
                tag = Image.ExifTags.TAGS.get(tag_id, tag_id)
                print(f"{tag}: {value}")
except Exception as e:
    print(f"Failed to process {image_path}: {e}")