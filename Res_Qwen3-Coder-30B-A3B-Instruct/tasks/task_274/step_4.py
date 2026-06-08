import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import Counter
from PIL import Image
import csv
import time
from io import BytesIO

# Let's try a different approach - use a website known to have images
base_url = "https://example.com"
visited_urls = set()
image_data = []
max_pages = 50

def get_page_content(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_images_from_page(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    
    image_urls = []
    for img in img_tags:
        src = img.get('src') or img.get('data-src') or img.get('data-original')
        if src:
            absolute_url = urljoin(base_url, src)
            # Filter out data URLs and invalid URLs
            if not absolute_url.startswith('data:') and 'http' in absolute_url:
                image_urls.append(absolute_url)
    
    return image_urls

def get_image_dimensions(image_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(image_url, timeout=10, headers=headers)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        return img.size  # Returns (width, height)
    except Exception as e:
        print(f"Error getting dimensions for {image_url}: {e}")
        return None

def crawl_website(start_url, max_pages=50):
    urls_to_visit = [start_url]
    visited_urls = set()
    page_count = 0
    
    while urls_to_visit and page_count < max_pages:
        current_url = urls_to_visit.pop(0)
        
        if current_url in visited_urls:
            continue
            
        visited_urls.add(current_url)
        print(f"Crawling: {current_url}")
        
        html_content = get_page_content(current_url)
        if not html_content:
            continue
            
        # Extract images from current page
        image_urls = extract_images_from_page(html_content, current_url)
        print(f"Found {len(image_urls)} images on this page")
        
        for img_url in image_urls:
            dimensions = get_image_dimensions(img_url)
            if dimensions:
                image_data.append({
                    'url': img_url,
                    'width': dimensions[0],
                    'height': dimensions[1]
                })
        
        # For this test, we'll just limit to the main page
        # In a real implementation, we would extract links and follow them
        break
        
        # Find more links to follow (simplified approach)
        # soup = BeautifulSoup(html_content, 'html.parser')
        # links = soup.find_all('a', href=True)
        # for link in links:
        #     href = link['href']
        #     absolute_url = urljoin(current_url, href)
        #     if absolute_url.startswith(base_url) and absolute_url not in visited_urls:
        #         urls_to_visit.append(absolute_url)
        
        page_count += 1
        time.sleep(1)  # Be respectful to the server
        
    return image_data

# Try with a simple example that has images
test_urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/webp"
]

print("Testing with direct image URLs...")
for url in test_urls:
    print(f"Testing URL: {url}")
    dimensions = get_image_dimensions(url)
    if dimensions:
        image_data.append({
            'url': url,
            'width': dimensions[0],
            'height': dimensions[1]
        })
        print(f"Dimensions: {dimensions}")

# Save to CSV
with open('image_dimensions.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['url', 'width', 'height']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for data in image_data:
        writer.writerow(data)

print(f"Collected {len(image_data)} images")
print("Data saved to image_dimensions.csv")

# Calculate most common dimensions
if image_data:
    dimensions_list = [(data['width'], data['height']) for data in image_data]
    dimension_counts = Counter(dimensions_list)