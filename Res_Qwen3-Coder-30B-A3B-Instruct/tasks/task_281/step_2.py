import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
from collections import defaultdict, Counter
import time

# Initialize variables
base_url = "https://docs.python.org/3/"
visited_urls = set()
links_graph = defaultdict(set)
page_data = {}
max_pages = 200

def is_valid_url(url):
    """Check if URL is valid and internal"""
    try:
        parsed = urlparse(url)
        return parsed.netloc == urlparse(base_url).netloc and parsed.scheme in ('http', 'https')
    except:
        return False

def get_page_content(url):
    """Fetch and parse page content"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_page_info(html_content, url):
    """Extract title, headings, and internal links from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract title
    title = soup.find('title')
    title_text = title.get_text().strip() if title else "No Title"
    
    # Extract headings (h1, h2, h3)
    headings = []
    for i in range(1, 4):
        for heading in soup.find_all(f'h{i}'):
            headings.append({
                'level': i,
                'text': heading.get_text().strip()
            })
    
    # Extract internal links
    internal_links = set()
    for link in soup.find_all('a', href=True):
        full_url = urljoin(url, link['href'])
        if is_valid_url(full_url):
            internal_links.add(full_url)
    
    return {
        'title': title_text,
        'headings': headings,
        'internal_links': list(internal_links)
    }

def crawl_website(start_url, max_pages=200):
    """Main crawling function"""
    urls_to_visit = [start_url]
    
    while urls_to_visit and len(visited_urls) < max_pages:
        current_url = urls_to_visit.pop(0)
        
        if current_url in visited_urls:
            continue
            
        print(f"Crawling: {current_url}")
        visited_urls.add(current_url)
        
        html_content = get_page_content(current_url)
        if not html_content:
            continue
            
        # Extract information
        info = extract_page_info(html_content, current_url)
        page_data[current_url] = info
        
        # Add new internal links to visit queue
        for link in info['internal_links']:
            if link not in visited_urls and link not in urls_to_visit:
                urls_to_visit.append(link)
        
        # Small delay to be respectful
        time.sleep(0.1)
    
    return True

# Start crawling
print("Starting crawl...")
crawl_website(base_url, max_pages)

print(f"Visited {len(visited_urls)} pages")
print("Crawling completed.")