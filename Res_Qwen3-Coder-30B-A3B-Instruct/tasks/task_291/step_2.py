import requests
from bs4 import BeautifulSoup
import networkx as nx
from community import community_louvain
import json
from collections import deque

# Initialize variables
start_url = "https://en.wikipedia.org/wiki/Main_Page"
max_pages = 300
visited = set()
graph = nx.Graph()
queue = deque([start_url])

print("Starting wiki crawl...")

# Crawl the wiki
while queue and len(visited) < max_pages:
    url = queue.popleft()
    
    if url in visited:
        continue
        
    try:
        # Fetch the page
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.find('h1', {'class': 'firstHeading'})
        if not title:
            continue
            
        page_title = title.text.strip()
        visited.add(url)
        print(f"Crawled: {page_title}")
        
        # Add node to graph
        graph.add_node(page_title)
        
        # Find all links
        links = soup.find_all('a', href=True)
        
        # Add edges to graph
        for link in links:
            href = link['href']
            
            # Only process internal wiki links
            if href.startswith('/wiki/') and ':' not in href:
                target_url = f"https://en.wikipedia.org{href}"
                target_title = href.replace('/wiki/', '')
                
                # Add edge to graph
                graph.add_edge(page_title, target_title)
                
                # Add to queue if not visited and we haven't reached max pages
                if target_url not in visited and len(visited) < max_pages:
                    queue.append(target_url)
                    
    except Exception as e:
        print(f"Error crawling {url}: {e}")
        continue

print(f"Finished crawling. Visited {len(visited)} pages.")

# Save graph to JSON
with open('wiki_graph.json', 'w') as f:
    data = {
        'nodes': list(graph.nodes()),
        'edges': list(graph.edges())
    }
    json.dump(data, f)

print("Graph saved to wiki_graph.json")

# Perform community detection
partition = community_louvain.best_partition(graph)
print(f"Found {len(set(partition.values()))} communities")

# Generate report
report = {
    'total_pages': len(visited),
    'total_links': graph.number_of_edges(),
    'communities': len(set(partition.values())),
    'largest_community_size': max(len([n for n, p in partition.items() if p == c]) 
                                  for c in set(partition.values()))
}

print("Report generated")
print(json.dumps(report, indent=2))

# Find and print the largest community
community_sizes = {}
for node, comm_id in partition.items():
    if comm_id not in community_sizes:
        community_sizes[comm_id] = []
    community_sizes[comm_id].append(node)

largest_community_id = max(community_sizes.keys(), key=lambda x: len(community_sizes[x]))
largest_community = community_sizes[largest_community_id]

print(f"Largest community ({len(largest_community)} nodes):")
for node in sorted(largest_community)[:10]:  # Print first 10 nodes
    print(f"  - {node}")