import networkx as nx
import json

# Load the cross-reference graph from JSON
with open('cross_reference_graph.json', 'r') as f:
    graph_data = json.load(f)

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
for source, targets in graph_data.items():
    for target in targets:
        G.add_edge(source, target)

# Identify disconnected documentation groups
connected_components = list(nx.weakly_connected_components(G))

# Save the connected components to JSON
with open('disconnected_groups.json', 'w') as f:
    json.dump(connected_components, f, indent=4)

print("Disconnected documentation groups saved to disconnected_groups.json")