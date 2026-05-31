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

# Step 6: Load the JSON data
with open('website_index.json', 'r') as f:
    data = json.load(f)

# Step 7: Flatten the list of headings into a single list
all_headings = [heading for item in data for heading in item['headings']]

# Step 8: Count the frequency of each heading
from collections import Counter
heading_counts = Counter(all_headings)

# Step 9: Check if there are any headings before finding the most common one
if heading_counts:
    most_common_heading, count = heading_counts.most_common(1)[0]
    print(f"The most common heading is '{most_common_heading}' with {count} occurrences.")
else:
    print("No headings found in the crawled data.")