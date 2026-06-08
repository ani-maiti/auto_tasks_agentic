import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
from collections import defaultdict

# Define the base URL to crawl
base_url = "https://docs.python.org/3/"
visited_urls = set()
internal_links = defaultdict(list)
external_links = set()

def is_internal_link(url, base_domain):
    return urlparse(url).netloc == base_domain or not urlparse(url).netloc

def get_all_links(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        links = []
        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            links.append(absolute_url)
        
        return links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []

def crawl_site(start_url, max_pages=100):
    domain = urlparse(start_url).netloc
    urls_to_visit = [start_url]
    visited_count = 0
    
    while urls_to_visit and visited_count < max_pages:
        current_url = urls_to_visit.pop(0)
        
        if current_url in visited_urls:
            continue
            
        visited_urls.add(current_url)
        visited_count += 1
        
        print(f"Crawling: {current_url}")
        
        links = get_all_links(current_url)
        current_page_links = []
        
        for link in links:
            if is_internal_link(link, domain):
                current_page_links.append(link)
                if link not in visited_urls and link not in urls_to_visit:
                    urls_to_visit.append(link)
            else:
                external_links.add(link)
        
        internal_links[current_url] = current_page_links
    
    return visited_urls, internal_links

# Start crawling
print("Starting crawl...")
visited_pages, all_links = crawl_site(base_url, max_pages=50)

# Count incoming links for each page
incoming_links = defaultdict(int)
for page, links in all_links.items():
    for link in links:
        if link in visited_pages:
            incoming_links[link] += 1

# Find orphan pages (pages with zero incoming links)
orphan_pages = []
for page in visited_pages:
    if incoming_links[page] == 0 and page != base_url:
        orphan_pages.append(page)

# Save results to JSON
results = {
    "total_pages": len(visited_pages),
    "orphan_pages_count": len(orphan_pages),
    "orphan_pages": orphan_pages,
    "external_links_count": len(external_links)
}

with open('crawl_results.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"Crawl completed. Total pages: {len(visited_pages)}")
print(f"Orphan pages found: {len(orphan_pages)}")
print(f"External links found: {len(external_links)}")