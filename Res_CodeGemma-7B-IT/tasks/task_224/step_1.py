import os
import datetime
from PIL import Image
from PIL.Exif import ImageFile

# Get all image files in the current directory
images = [f for f in os.listdir('.') if f.endswith(('.jpg', '.jpeg', '.png'))]

# Initialize variables for the oldest image and its timestamp
oldest_image = None
oldest_timestamp = datetime.datetime.now()

# Iterate through the images
for image in images:
    # Open the image
    with Image.open(image) as img:
        # Get the image's creation or modification timestamp
        timestamp = img._getexif()[36867] if img.format == 'JPEG' else img.stat().st_mtime

        # Check if this image is older than the current oldest image
        if timestamp < oldest_timestamp:
            oldest_image = image
            oldest_timestamp = timestamp

# Print the metadata summary report
print('Metadata Summary Report:')
for image in images:
    with Image.open(image) as img:
        metadata = img._getexif() if img.format == 'JPEG' else None
        print(f'{image}:')
        if metadata:
            for tag, value in metadata.items():
                if tag in ImageFile.TAGS:
                    print(f'  {ImageFile.TAGS[tag]}: {value}')
        else:
            print('  No metadata available')

# Print the oldest image
print(f'Oldest image: {oldest_image}')