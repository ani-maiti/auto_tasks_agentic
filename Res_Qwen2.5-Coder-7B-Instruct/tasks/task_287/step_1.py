import os
from PIL import Image
import json

# Step 1: Discover all image files in the current directory
image_files = [f for f in os.listdir('.') if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
print(f"Found {len(image_files)} image files.")