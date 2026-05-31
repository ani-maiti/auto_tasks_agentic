import networkx as nx
import json

# Load the graph from JSON
with open('page_graph.json', 'r') as f:
    graph_dict = json.load(f)

# Create a directed graph
graph = nx.from_dict_of_lists(graph_dict)

# Identify communities using Girvan-Newman algorithm
communities = list(nx.algorithms.community.girvan_newman(graph))
highest_modularity = -1
best_partition = []

for modularity, partition in communities:
    if modularity > highest_modularity:
        highest_modularity = modularity
        best_partition = partition

# Find the largest community
largest_community = max(best_partition, key=len)

# Print the largest community
print("Largest community:", largest_community)