import requests
from bs4 import BeautifulSoup
import re

# Define the base URL and the number of pages to crawl
base_url = "https://example.com"
num_pages = 50

# Initialize a list to store image URLs
image_urls = []

# Loop through the pages and extract image URLs
for page_num in range(1, num_pages + 1):
    url = f"{base_url}/page/{page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <img> tags and extract the src attribute
    img_tags = soup.find_all('img')
    for tag in img_tags:
        img_url = tag.get('src')
        if img_url:
            image_urls.append(img_url)

print(f"Collected {len(image_urls)} image URLs.")
```

This script will crawl up to 50 pages of a specified website and collect all image URLs. It uses the `requests` library to fetch web pages and `BeautifulSoup` to parse HTML content. The collected image URLs are stored in a list.