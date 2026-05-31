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
```
execution trace:
stdout:
Metadata Summary Report:
nasa_image_1.jpg:
  DateTimeOriginal: 2023:03:08 00:00:00
  Model: Canon EOS 5D Mark IV
  ExifImageWidth: 5184
  ExifImageHeight: 3456
  ExifExifOffset: 0
  ExifInteroperabilityOffset: 0
  ExifOffset: 0
  ExifSubIFDOffset: 0
  ExifCompressedBitsPerPixel: 8
  ExifPixelXDimension: 5184
  ExifPixelYDimension: 3456
  ExifRelatedImageFileFormat: JPEG
  ExifRelatedImageWidth: 5184
  ExifRelatedImageHeight: 3456
  ExifExifVersion: 0220
  ExifFlashpixVersion: 0220
  ExifColorSpace: sRGB
  ExifExifCompression: JPEG (old)
  ExifInteroperabilityIndex: 0x4D4D
  ExifDateTimeOriginal: 2023:03:08 00:00:00
  ExifDateTimeDigitized: 2023:03:08 00:00:00
  ExifDateTime: 2023:03:08 00:00:00
  ExifDateTimeUnspecified: 2023:03:08 00:00:00
  ExifOffsetTimeOriginal: 0
  ExifOffsetTimeDigitized: 0
  ExifOffsetTime: 0
  ExifOffsetDateTime: 0
  ExifOffsetDateTimeUnspecified: 0
  ExifOffsetTimeOriginalSeconds: 0
  ExifOffsetTimeDigitizedSeconds: 0
  ExifOffsetDateTimeSeconds: 0
  ExifOffsetDateTimeUnspecifiedSeconds: 0
  ExifSubSecTimeOriginal: 0
  ExifSubSecTimeDigitized: 0
  ExifSubSecDateTime: 0
  ExifSubSecDateTimeUnspecified: 0
  ExifExifOffsetTimeOriginal: 0
  ExifExifOffsetTimeDigitized: 0
  ExifExifOffsetDateTime: 0
  ExifExifOffsetDateTimeUnspecified: 0
  ExifExifOffsetTimeOriginalSeconds: 0
  ExifExifOffsetTimeDigitizedSeconds: 0
  ExifExifOffsetDateTimeSeconds: 0
  ExifExifOffsetDateTimeUnspecifiedSeconds: 0
  ExifExifOffsetSubSecTimeOriginal: 0
  ExifExifOffsetSubSecTimeDigitized: 0
  ExifExifOffsetSubSecDateTime: 0
  ExifExifOffsetSubSecDateTimeUnspecified: 0
  ExifExifOffsetExifOffsetTimeOriginal: 0
  ExifExifOffsetExifOffsetTimeDigitized: 0
  ExifEx