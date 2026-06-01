import networkx as nx
import json
from community import community_louvain

# Load the graph from JSON
with open('wiki_graph.json', 'r') as f:
    data = json.load(f)
graph = nx.node_link_graph(data)

# Identify communities using the Louvain method
partition = community_louvain.best_partition(graph)

# Create a dictionary to store communities
communities = {}
for node, com in partition.items():
    communities.setdefault(com, []).append(node)

# Find the largest community
largest_community = max(communities, key=lambda x: len(communities[x]))

# Generate a report
report = {
    "total_nodes": graph.number_of_nodes(),
    "total_edges": graph.number_of_edges(),
    "number_of_communities": len(communities),
    "largest_community_size": len(communities[largest_community]),
    "largest_community": communities[largest_community]
}

# Save the report to a file
with open('report.json', 'w') as f:
    json.dump(report, f)

# Print the largest community
print("Largest Community:")
for page in report["largest_community"]:
    print(page)