# Build the link graph from the crawled data
for url, data in page_data.items():
    for link in data['internal_links']:
        if link in page_data:  # Only add links to pages we've crawled
            links_graph[url].add(link)

# Save the graph to JSON
with open('link_graph.json', 'w') as f:
    json.dump(dict(links_graph), f, indent=2)

print("Link graph saved to link_graph.json")
print(f"Total pages crawled: {len(visited_urls)}")
print(f"Total links in graph: {sum(len(links) for links in links_graph.values())}")