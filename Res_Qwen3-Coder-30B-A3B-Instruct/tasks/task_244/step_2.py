import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict
import re
import time

# Use a more accessible starting page
start_page = "https://en.wikipedia.org/wiki/Main_Page"

# Initialize data structures
link_graph = defaultdict(list)
visited_pages = set()
pages_to_visit = [start_page]
collected_pages = 0

print("Starting wiki crawl with Main_Page...")

while collected_pages < 50 and pages_to_visit:
    current_url = pages_to_visit.pop(0)
    
    if current_url in visited_pages:
        continue
        
    try:
        # Add headers to mimic a real browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(current_url, headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract page title
        title = soup.find('h1', {'class': 'firstHeading'})
        if title:
            page_title = title.text
        else:
            page_title = current_url.split('/')[-1]
            
        # Find all links
        links = soup.find_all('a', href=re.compile(r'^/wiki/'))
        
        # Add links to graph
        for link in links:
            href = link.get('href')
            if href and ':' not in href:  # Skip special pages
                # Convert relative URL to absolute
                abs_url = f"https://en.wikipedia.org{href}"
                link_graph[current_url].append(abs_url)
                
                # Add to queue if we haven't visited it yet
                if abs_url not in visited_pages and abs_url not in pages_to_visit:
                    pages_to_visit.append(abs_url)
                    
        visited_pages.add(current_url)
        collected_pages += 1
        
        if collected_pages % 10 == 0:
            print(f"Collected {collected_pages} pages...")
            
        # Be respectful to the server
        time.sleep(0.1)
            
    except Exception as e:
        print(f"Error processing {current_url}: {e}")
        continue

print(f"Finished crawling. Collected {collected_pages} pages.")

# Save link graph to JSON
with open('link_graph.json', 'w') as f:
    json.dump(dict(link_graph), f, indent=2)

print("Link graph saved to link_graph.json")

# Find page with highest degree
max_degree = 0
most_connected_page = None

for page, links in link_graph.items():
    degree = len(links)
    if degree > max_degree:
        max_degree = degree
        most_connected_page = page

print(f"Page with highest degree: {most_connected_page}")
print(f"Highest degree: {max_degree}")