import os
import subprocess
from datetime import datetime
import json

# Find all image files
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
image_files = []

for root, dirs, files in os.walk("/home"):
    for file in files:
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(os.path.join(root, file))

# Extract metadata for each image
metadata_list = []
for image_path in image_files[:10]:  # Limit to first 10 for demo
    try:
        # Use exiftool if available, otherwise fallback to basic info
        result = subprocess.run(['exiftool', '-json', image_path], capture_output=True, text=True)
        if result.returncode == 0:
            metadata = json.loads(result.stdout)
            metadata_list.append({
                'path': image_path,
                'metadata': metadata[0] if isinstance(metadata, list) else metadata
            })
        else:
            # Fallback to basic file info
            stat_info = os.stat(image_path)
            metadata_list.append({
                'path': image_path,
                'metadata': {
                    'File Size': stat_info.st_size,
                    'Created Time': datetime.fromtimestamp(stat_info.st_ctime).isoformat(),
                    'Modified Time': datetime.fromtimestamp(stat_info.st_mtime).isoformat()
                }
            })
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Generate summary report
print("=== IMAGE METADATA SUMMARY REPORT ===")
print(f"Total images found: {len(image_files)}")
print("\nFirst 10 images with metadata:")
for item in metadata_list:
    print(f"\nPath: {item['path']}")
    meta = item['metadata']
    for key, value in meta.items():
        if not key.startswith('File'):
            print(f"  {key}: {value}")

# Find oldest image
oldest_image = min(image_files, key=lambda f: os.path.getctime(f))
print(f"\n=== OLDEST IMAGE ===")
print(f"Path: {oldest_image}")
print(f"Created Time: {datetime.fromtimestamp(os.path.getctime(oldest_image)).isoformat()}")