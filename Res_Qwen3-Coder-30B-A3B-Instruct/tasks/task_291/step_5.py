import json

# Read and display the graph data
with open('wiki_graph.json', 'r') as f:
    graph_data = json.load(f)

print(f"Total nodes: {len(graph_data['nodes'])}")
print(f"Total edges: {len(graph_data['edges'])}")

# Show first few nodes and edges
print("\nFirst 10 nodes:")
for node in graph_data['nodes'][:10]:
    print(f"  {node}")

print("\nFirst 10 edges:")
for edge in graph_data['edges'][:10]:
    print(f"  {edge}")

# Display the report
with open('report.txt', 'w') as f:
    f.write(json.dumps({
        'total_pages': len(graph_data['nodes']),
        'total_links': len(graph_data['edges'])
    }, indent=2))

print("\nReport saved to report.txt")