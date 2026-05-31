import requests
from bs4 import BeautifulSoup
import csv
from collections import Counter

# Define the URL of the website to crawl
url = 'https://example.com'

# Function to extract image URLs from a page
def extract_image_urls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    return [img['src'] for img in img_tags if 'src' in img.attrs]

# List to store all image URLs
all_image_urls = []

# Crawl up to 50 pages
for i in range(1, 51):
    page_url = f'{url}?page={i}'
    image_urls = extract_image_urls(page_url)
    all_image_urls.extend(image_urls)

# Save the collected image URLs to a CSV file
with open('image_urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Image URL'])
    writer.writerows([[url] for url in all_image_urls])

print("Collected image URLs and saved to image_urls.csv")