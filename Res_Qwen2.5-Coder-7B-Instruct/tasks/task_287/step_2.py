# Step 2: Extract dimensions, format, and metadata from each image file
image_data = []
for file in image_files:
    try:
        with Image.open(file) as img:
            width, height = img.size
            format_ = img.format
            metadata = img.info
            image_data.append({
                'file': file,
                'width': width,
                'height': height,
                'format': format_,
                'metadata': metadata
            })
    except Exception as e:
        print(f"Error processing {file}: {e}")
print(f"Extracted data for {len(image_data)} images.")