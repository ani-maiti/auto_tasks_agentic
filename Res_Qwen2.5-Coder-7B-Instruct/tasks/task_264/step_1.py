import requests
from bs4 import BeautifulSoup
import json

# Step 1: Define the base URL of the documentation site
base_url = "https://example.com/docs"

# Step 2: Fetch the homepage to start crawling
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract all internal links from the homepage
internal_links = set()
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.startswith('/docs'):
        internal_links.add(href)

# Step 4: Print the collected internal links
print(internal_links)
```

This code will fetch the homepage of the documentation site, extract all internal links, and print them. The next step would involve recursively fetching these links and collecting more internal links until no new links are found.