import requests
from bs4 import BeautifulSoup
import networkx as nx
import json

# Define the starting URL
start_url = "https://en.wikipedia.org/wiki/Web_scraping"

# Function to fetch a page and extract links
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        return None

# Function to extract all internal links from a page
def get_links(soup):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/') and ':' not in href:
            links.append(href[6:])
    return links

# Initialize the graph
graph = nx.DiGraph()

# List to keep track of visited pages
visited_pages = set()
queue = [start_url]

while queue and len(visited_pages) < 300:
    current_url = queue.pop(0)
    if current_url not in visited_pages:
        visited_pages.add(current_url)
        soup = fetch_page(f"https://en.wikipedia.org/wiki/{current_url}")
        if soup:
            for link in get_links(soup):
                if link not in visited_pages and link not in queue:
                    queue.append(link)
                    graph.add_edge(current_url, link)

# Convert the graph to a dictionary before saving
graph_dict = {node: list(graph.neighbors(node)) for node in graph.nodes}

# Save the graph to JSON
with open('page_graph.json', 'w') as f:
    json.dump(graph_dict, f)

print("Graph saved to page_graph.json")