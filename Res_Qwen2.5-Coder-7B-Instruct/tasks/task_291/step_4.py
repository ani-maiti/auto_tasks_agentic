import networkx as nx
import json

# Load the graph from JSON
with open('page_graph.json', 'r') as f:
    graph_dict = json.load(f)

# Create a directed graph
graph = nx.from_dict_of_lists(graph_dict)

# Identify communities using Louvain algorithm
communities = list(nx.algorithms.community.louvain_communities(graph))

# Check if there are communities found
if communities:
    # Find the largest community
    largest_community = max(communities, key=len)
    # Print the largest community
    print("Largest community:", largest_community)
else:
    print("No communities found.")