import requests
from PIL import Image
from io import BytesIO
import csv
from collections import Counter

# Function to get image dimensions
def get_image_dimensions(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img.width, img.height

# Dictionary to store image dimensions
image_dimensions = {}

# Read image URLs from CSV
with open('image_urls.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    for row in reader:
        image_url = row[0]
        try:
            width, height = get_image_dimensions(image_url)
            image_dimensions[(width, height)] = image_dimensions.get((width, height), 0) + 1
        except Exception as e:
            print(f"Error fetching {image_url}: {e}")

# Identify the most common image dimensions
most_common_dimensions = Counter(image_dimensions).most_common()

# Save the most common image dimensions to a CSV file
with open('common_image_dimensions.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Width', 'Height', 'Count'])
    writer.writerows(most_common_dimensions)

print("Identified most common image dimensions and saved to common_image_dimensions.csv")