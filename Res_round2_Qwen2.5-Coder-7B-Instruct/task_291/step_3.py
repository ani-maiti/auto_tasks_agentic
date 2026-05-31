import requests
from bs4 import BeautifulSoup
import networkx as nx
import json

# Step 1: Define the starting URL
starting_url = "https://en.wikipedia.org/wiki/Web_scraping"

# Step 2: Function to fetch the HTML content of a given URL
def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Step 3: Function to extract links from HTML content
def extract_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

# Step 4: Function to filter out internal Wikipedia links
def filter_internal_links(links):
    internal_links = [link for link in links if '/wiki/' in link]
    return internal_links

# Step 5: Initialize the graph
graph = nx.DiGraph()

# Step 6: Crawl the wiki and build the graph
visited_pages = set()
queue = [starting_url]

while queue and len(visited_pages) < 300:
    url = queue.pop(0)
    if url not in visited_pages:
        html = fetch_html(url)
        if html:
            links = extract_links(html)
            internal_links = filter_internal_links(links)
            for link in internal_links:
                if link not in visited_pages:
                    graph.add_edge(url, link)
                    queue.append(link)
            visited_pages.add(url)

# Step 7: Save the graph to JSON
if hasattr(nx, 'write_json'):
    nx.write_json(graph, 'wiki_graph.json')
else:
    print("NetworkX write_json function not available.")

print("Graph saved attempt completed.")