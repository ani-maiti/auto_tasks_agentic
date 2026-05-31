import requests
from bs4 import BeautifulSoup
import json

# Step 1: Define the base URL to crawl
base_url = "https://example.com"

# Step 2: Function to fetch a page
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Step 3: Function to parse a page and extract title and headings
def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else ""
    headings = [h.text for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
    return title, headings

# Step 4: Crawl the website and collect data
data = []
for i in range(1, 101):  # Assuming we want to crawl up to 100 pages
    url = f"{base_url}/page/{i}"
    html = fetch_page(url)
    if html:
        title, headings = parse_page(html)
        data.append({'url': url, 'title': title, 'headings': headings})

# Step 5: Save the collected data to a JSON file
with open('website_index.json', 'w') as f:
    json.dump(data, f, indent=4)

print("Data saved to website_index.json")