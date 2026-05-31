import json
from collections import defaultdict

# Construct a cross-reference graph using links between files
graph = defaultdict(list)

files = [
    "./cpython/InternalDocs/structure.md",
    "./cpython/InternalDocs/stack_protection.md",
    # ... (list all Markdown files here)
    "./command_report.md"
]

for file in files:
    with open(file, 'r') as f:
        content = f.read()
        for other_file in files:
            if other_file != file and other_file in content:
                graph[file].append(other_file)
                graph[other_file].append(file)

# Save the graph to JSON
with open('cross_reference_graph.json', 'w') as f:
    json.dump(graph, f, indent=4)

print("Cross-reference graph saved to cross_reference_graph.json")