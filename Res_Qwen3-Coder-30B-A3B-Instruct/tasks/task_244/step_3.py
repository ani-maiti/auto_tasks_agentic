import json

# Load the saved link graph
with open('link_graph.json', 'r') as f:
    link_graph = json.load(f)

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

# Print some statistics
total_pages = len(link_graph)
total_links = sum(len(links) for links in link_graph.values())
avg_links_per_page = total_links / total_pages if total_pages > 0 else 0

print(f"Total pages crawled: {total_pages}")
print(f"Total links found: {total_links}")
print(f"Average links per page: {avg_links_per_page:.2f}")