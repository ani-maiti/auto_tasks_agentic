import os
from PIL import Image

image_path = './histogram.png'
with Image.open(image_path) as img:
    exif_data = img._getexif()
    if exif_data:
        print(f"Metadata for {image_path}:")
        for tag_id, value in exif_data.items():
            tag = Image.ExifTags.TAGS.get(tag_id, tag_id)
            print(f"{tag}: {value}")
```

This script attempts to open the image file and extract its EXIF data. If successful, it prints out the metadata. If there's no EXIF data, it will simply pass without printing anything.