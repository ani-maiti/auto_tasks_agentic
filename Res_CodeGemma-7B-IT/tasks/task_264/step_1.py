import requests
from bs4 import BeautifulSoup
import json

# Set the website URL
url = "https://example.com/docs/"

# Initialize lists for internal links and orphan pages
internal_links = []
orphan_pages = []

# Function to crawl a given URL and extract internal links
def crawl(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a", href=True):
        if link.get("href").startswith("/docs/"):
            internal_links.append(link.get("href"))

# Function to identify orphan pages
def identify_orphans():
    for link in internal_links:
        if link not in seen_links:
            orphan_pages.append(link)

# Initialize set of seen links
seen_links = set()

# Start crawling and identifying orphans
crawl(url)
identify_orphans()

# Save orphan pages to JSON file
with open("orphan_pages.json", "w") as f:
    json.dump(orphan_pages, f)

# Print a message
print("Orphan pages saved to orphan_pages.json")
```

**Note:**

* This code requires the `requests` and `beautifulsoup4` libraries to be installed.
* The website URL needs to be replaced with the actual documentation site you want to crawl.
* The output file name `orphan_pages.json` can be changed as needed.