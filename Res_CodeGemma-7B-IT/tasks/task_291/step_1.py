from urllib.request import urlopen
from bs4 import BeautifulSoup
import networkx as nx

# Set the starting page
start_page = "https://en.wikipedia.org/wiki/Main_Page"

# Set the maximum number of pages to collect
max_pages = 300

# Create an empty graph
graph = nx.Graph()

# Function to crawl a page and extract links
def crawl_page(url):
    response = urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all("a", href=True):
        if link.get("href").startswith("/wiki/"):
            full_url = "https://en.wikipedia.org" + link.get("href")
            graph.add_edge(url, full_url)
            if len(graph) <= max_pages:
                crawl_page(full_url)

# Start the crawling process
crawl_page(start_page)

# Save the graph to JSON
nx.write_graphml(graph, "wikipedia_graph.graphml")

# Identify communities using graph analysis
communities = nx.community.greedy_modularity_communities(graph)

# Print the largest community
largest_community = max(communities, key=len)
print("Largest community:")
for page in largest_community:
    print(page)