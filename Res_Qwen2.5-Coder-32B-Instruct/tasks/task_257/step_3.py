import imagehash
from PIL import Image
import csv

def compute_perceptual_hash(image_path):
    try:
        with Image.open(image_path) as img:
            return str(imagehash.phash(img))
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

image_files = open('image_files.txt', 'r').read().splitlines()
hashes = {}

for image_file in image_files:
    hash_value = compute_perceptual_hash(image_file)
    if hash_value:
        if hash_value not in hashes:
            hashes[hash_value] = []
        hashes[hash_value].append(image_file)

with open('image_hashes.csv', 'w', newline='') as csvfile:
    fieldnames = ['hash', 'files']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for hash_value, files in hashes.items():
        writer.writerow({'hash': hash_value, 'files': ', '.join(files)})

print("Perceptual hashes computed and saved to image_hashes.csv")