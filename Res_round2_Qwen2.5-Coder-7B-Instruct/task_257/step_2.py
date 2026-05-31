import os
from PIL import Image
import imagehash

# Dictionary to store perceptual hashes of images
image_hashes = {}

# Process each image file found
for root, _, files in os.walk('.'):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(root, file)
            try:
                with Image.open(file_path) as img:
                    hash_value = str(imagehash.average_hash(img))
                    if hash_value in image_hashes:
                        image_hashes[hash_value].append(file_path)
                    else:
                        image_hashes[hash_value] = [file_path]
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Save results to CSV
with open('duplicate_images.csv', 'w') as csvfile:
    for hash_value, paths in image_hashes.items():
        if len(paths) > 1:
            csvfile.write(','.join(paths) + '\n')

# Print the largest duplicate group
largest_group = max(image_hashes.values(), key=len)
print("Largest duplicate group:")
for path in largest_group:
    print(path)