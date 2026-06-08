import os
import hashlib
from PIL import Image
import numpy as np
import pandas as pd
from scipy.spatial.distance import hamming
import itertools

# Create a function to compute perceptual hash
def dhash(image_path, hash_size=8):
    # Open image and convert to grayscale
    image = Image.open(image_path)
    if image.mode != 'L':
        image = image.convert('L')
    
    # Resize image to hash_size + 1 x hash_size
    image = image.resize((hash_size + 1, hash_size), Image.LANCZOS)
    
    # Compute difference hash
    pixels = list(image.getdata())
    hash_bits = []
    for i in range(hash_size):
        for j in range(hash_size):
            left = pixels[i * (hash_size + 1) + j]
            right = pixels[i * (hash_size + 1) + j + 1]
            hash_bits.append(1 if left > right else 0)
    
    # Convert bits to hexadecimal string
    hash_str = ''.join(str(bit) for bit in hash_bits)
    return hash_str

# Find all image files
image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}
image_files = []

for root, dirs, files in os.walk('.'):
    for file in files:
        if os.path.splitext(file)[1].lower() in image_extensions:
            image_files.append(os.path.join(root, file))

print(f"Found {len(image_files)} image files")
```