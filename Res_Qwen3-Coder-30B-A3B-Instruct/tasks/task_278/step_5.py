# Build relationship graph
graph = defaultdict(list)

for rel in relationships:
    file1 = rel['file1']
    file2 = rel['file2']
    graph[file1].append(file2)
    graph[file2].append(file1)

# Compute connected components
def find_connected_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            # BFS to find connected component
            component = []
            queue = deque([node])
            visited.add(node)
            
            while queue:
                current = queue.popleft()
                component.append(current)
                
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            components.append(component)
    
    return components

connected_components = find_connected_components(graph)

print("Connected components:")
for i, component in enumerate(connected_components):
    print(f"Component {i+1}: {component}")

# Find the largest connected component
largest_component = max(connected_components, key=len)
print(f"\nLargest connected component: {largest_component}")

# Save graph structure to JSON
with open('relationship_graph.json', 'w') as f:
    json.dump(dict(graph), f, indent=2)

print("\nGraph saved to relationship_graph.json")