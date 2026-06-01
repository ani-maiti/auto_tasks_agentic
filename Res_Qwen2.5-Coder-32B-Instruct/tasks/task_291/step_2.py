import requests
from bs4 import BeautifulSoup
import networkx as nx
import json

# Define the starting URL and the maximum number of pages to crawl
start_url = "https://en.wikipedia.org/wiki/Web_scraping"
max_pages = 300

# Initialize a set to keep track of visited URLs and a graph
visited_urls = set()
graph = nx.Graph()

# Function to get all links from a given Wikipedia page
def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = set()
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/wiki/') and ':' not in href:
            full_url = f"https://en.wikipedia.org{href}"
            links.add(full_url)
    return links

# Function to perform BFS and build the graph
def crawl_wiki(start_url, max_pages):
    queue = [start_url]
    while queue and len(visited_urls) < max_pages:
        current_url = queue.pop(0)
        if current_url not in visited_urls:
            visited_urls.add(current_url)
            print(f"Visiting: {current_url}")
            new_links = get_links(current_url)
            graph.add_node(current_url)
            for link in new_links:
                graph.add_edge(current_url, link)
                if link not in visited_urls:
                    queue.append(link)

# Start crawling
crawl_wiki(start_url, max_pages)

# Save the graph to JSON
data = nx.node_link_data(graph)
with open('wiki_graph.json', 'w') as f:
    json.dump(data, f)

print("Graph saved to wiki_graph.json")