# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import csv

# Set website URL and page limit
url = "https://www.example.com/"
page_limit = 50

# Initialize variables
image_urls = []
image_dimensions = {}

# Function to extract image URLs from a given page
def extract_image_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    for img in soup.find_all("img"):
        image_urls.append(img.get("src"))

# Function to get image dimensions from a given URL
def get_image_dimensions(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    return image.width, image.height

# Crawl website and extract image URLs
for page_number in range(1, page_limit + 1):
    response = requests.get(url + f"page-{page_number}")
    extract_image_urls(response.text)

# Get image dimensions and store results
for url in image_urls:
    try:
        width, height = get_image_dimensions(url)
        image_dimensions[url] = (width, height)
    except Exception:
        pass

# Save results to CSV
with open("image_dimensions.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Image URL", "Width", "Height"])
    for url, dimensions in image_dimensions.items():
        writer.writerow([url, dimensions[0], dimensions[1]])