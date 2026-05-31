# List all image files in the current directory and subdirectories
images = [f for f in os.listdir('.') if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Function to extract metadata from an image
def extract_metadata(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                return {Image.ExifTags.TAGS.get(tag_id, tag_id): value for tag_id, value in exif_data.items()}
            else:
                return {}
    except Exception as e:
        print(f"Failed to process {image_path}: {e}")
        return {}

# Extract metadata for each image
metadata_list = [extract_metadata(os.path.join('.', img)) for img in images]

# Print the extracted metadata
for i, metadata in enumerate(metadata_list):
    print(f"Metadata for {images[i]}:")
    for key, value in metadata.items():
        print(f"  {key}: {value}")
    print()

# Identify the oldest image by timestamp
oldest_image = None
oldest_timestamp = None
for i, metadata in enumerate(metadata_list):
    if 'DateTimeOriginal' in metadata:
        timestamp = datetime.datetime.strptime(metadata['DateTimeOriginal'], '%Y:%m:%d %H:%M:%S')
        if oldest_timestamp is None or timestamp < oldest_timestamp:
            oldest_timestamp = timestamp
            oldest_image = images[i]

if oldest_image:
    print(f"The oldest image is {oldest_image} with timestamp {oldest_timestamp}.")
else:
    print("No images found with DateTimeOriginal metadata.")