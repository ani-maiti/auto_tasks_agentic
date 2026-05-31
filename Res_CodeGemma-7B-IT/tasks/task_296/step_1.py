# Import libraries
import os
import networkx as nx

# Find all Python files in the current directory
python_files = [f for f in os.listdir(".") if f.endswith(".py")]

# Build a function call graph
graph = nx.DiGraph()
for file in python_files:
    with open(file, "r") as f:
        for line in f:
            if line.startswith("def ") and "(" in line:
                function_name = line.split("(")[0].strip()
                graph.add_node(function_name)
            elif line.startswith("    ") and "(" in line:
                callee = line.split("(")[0].strip()
                graph.add_edge(function_name, callee)

# Identify strongly connected components and recursive structures
components = nx.strongly_connected_components(graph)
recursive_components = [c for c in components if c.is_directed_acyclic_graph()]

# Save the graph to JSON
nx.write_graphml(graph, "function_call_graph.graphml")

# Generate a report
report = f"""
## Function Call Graph Report

**Number of Python files:** {len(python_files)}
**Number of functions:** {len(graph.nodes)}
**Number of components:** {len(components)}
**Number of recursive components:** {len(recursive_components)}

**Largest component:**

* Nodes: {len(max(components, key=len))}
* Functions: {", ".join(max(components, key=len))}
"""

# Print the report
print(report)

# Print the largest component
print("Largest component:")
for function in max(components, key=len):
    print(function)