import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import Counter

# Start with a public website - let's use python.org as an example
base_url = "https://docs.python.org/3/"
visited_urls = set()
page_titles = []
max_pages = 50

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def get_page_title(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            return title_tag.get_text().strip()
        return "No Title Found"
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return "Error"

def extract_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, link['href'])
        if is_valid_url(absolute_url) and base_url in absolute_url:
            links.append(absolute_url)
    return links

print("Starting crawl...")
response = requests.get(base_url)
if response.status_code != 200:
    print("Failed to fetch homepage")
else:
    # Get initial page title
    initial_title = get_page_title(base_url)
    page_titles.append((base_url, initial_title))
    visited_urls.add(base_url)
    
    # Extract links from homepage
    links = extract_links(response.content, base_url)
    print(f"Found {len(links)} links on homepage")
    
    # Crawl additional pages
    for i, link in enumerate(links):
        if len(page_titles) >= max_pages:
            break
        if link in visited_urls:
            continue
            
        title = get_page_title(link)
        page_titles.append((link, title))
        visited_urls.add(link)
        
        # Print progress
        if (i + 1) % 10 == 0:
            print(f"Crawled {i + 1} pages")

print(f"Collected {len(page_titles)} page titles")

# Analyze collected titles for duplicates
titles_only = [title for _, title in page_titles]
title_counts = Counter(titles_only)

# Find duplicate titles
duplicate_titles = {title: count for title, count in title_counts.items() if count > 1}

print("Duplicate titles found:")
for title, count in duplicate_titles.items():
    print(f"  '{title}' appears {count} times")

# Generate report
print("\n--- REPORT ---")
print(f"Total pages crawled: {len(page_titles)}")
print(f"Unique titles: {len(set(titles_only))}")
print(f"Duplicate titles: {len(duplicate_titles)}")

# Show some sample data
print("\nSample of collected titles:")
for i, (url, title) in enumerate(page_titles[:10]):
    print(f"  {i+1}. {title}")

# Save results to file
with open('crawl_report.txt', 'w') as f:
    f.write("Website Crawl Report\n")
    f.write("====================\n\n")
    f.write(f"Total pages crawled: {len(page_titles)}\n")
    f.write(f"Unique titles: {len(set(titles_only))}\n")
    f.write(f"Duplicate titles: {len(duplicate_titles)}\n\n")
    
    if duplicate_titles:
        f.write("Duplicate titles:\n")
        for title, count in duplicate_titles.items():
            f.write(f"  '{title}' appears {count} times\n")
        f.write("\n")
    
    f.write("All page titles:\n")
    for url, title in page_titles:
        f.write(f"  {title}\n")

print("\nReport saved to crawl_report.txt")