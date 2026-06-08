import requests
from bs4 import BeautifulSoup
import json
from collections import Counter
import re

# Let's use a website with many pages for this example
# We'll use the Python documentation as it has many pages
base_url = "https://docs.python.org/3/"
start_page = base_url + "index.html"

# Function to extract title and headings from a page
def extract_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.find('title')
        title_text = title.get_text().strip() if title else ""
        
        # Extract headings (h1, h2, h3)
        headings = []
        for i in range(1, 4):
            for heading in soup.find_all(f'h{i}'):
                heading_text = heading.get_text().strip()
                if heading_text:
                    headings.append(heading_text)
        
        return {
            'url': url,
            'title': title_text,
            'headings': headings
        }
    except Exception as e:
        print(f"Error processing {url}: {e}")
        return None

# Function to find all links from a page
def get_links(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute URLs
            if href.startswith('/'):
                full_url = base_url.rstrip('/') + href
            elif href.startswith('http'):
                full_url = href
            else:
                continue
            
            # Only include links to the same domain
            if base_url in full_url:
                links.append(full_url)
        
        return list(set(links))  # Remove duplicates
    except Exception as e:
        print(f"Error getting links from {url}: {e}")
        return []

# Crawl the website
print("Starting crawl...")
all_pages = set([start_page])
visited = set()

# Limit to 100 pages for this example
max_pages = 100
current_count = 0

# Get initial links
links_to_visit = get_links(start_page)

while links_to_visit and current_count < max_pages:
    next_url = links_to_visit.pop()
    
    if next_url in visited or next_url in all_pages:
        continue
    
    all_pages.add(next_url)
    visited.add(next_url)
    current_count += 1
    
    print(f"Crawled {current_count}: {next_url}")
    
    # Get new links from this page
    new_links = get_links(next_url)
    links_to_visit.extend(new_links)
    
    # Limit the number of links we keep in memory
    if len(links_to_visit) > 1000:
        links_to_visit = links_to_visit[:1000]

print(f"Total pages crawled: {len(all_pages)}")

# Extract content from all pages
index = []
for page_url in all_pages:
    content = extract_content(page_url)
    if content:
        index.append(content)

print(f"Content extracted from {len(index)} pages")

# Save index to JSON
with open('search_index.json', 'w') as f:
    json.dump(index, f, indent=2)

print("Index saved to search_index.json")

# Generate report
all_headings = [heading for page in index for heading in page['headings']]
heading_counts = Counter(all_headings)

# Print most common headings
print("\nMost common headings:")
for heading, count in heading_counts.most_common(10):
    print(f"{count}: {heading}")

# Print report summary
print(f"\nReport Summary:")
print(f"- Total pages indexed: {len(index)}")
print(f"- Total unique headings: {len(heading_counts)}")
print(f"- Most common heading: '{heading_counts.most_common(1)[0][0]}' (appears {heading_counts.most_common(1)[0][1]} times)")