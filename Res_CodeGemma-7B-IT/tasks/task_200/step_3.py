import os
import ast
import networkx as nx

# Get all Python files in the current directory and subdirectories
python_files = [f for f in os.listdir(".") if f.endswith(".py")]

# Create an empty graph
graph = nx.DiGraph()

# Iterate over Python files and extract import statements
for file in python_files:
    with open(file, "r") as f:
        tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    graph.add_edge(alias.name, file)

# Identify the most imported modules
most_imported = [node for node, degree in sorted(graph.degree(), key=lambda x: x[1], reverse=True)[:10]]

# Generate a report
report = f"Top 10 most imported modules:\n\n"
for module in most_imported:
    report += f"- {module}\n"

# Save the graph in Graphviz format
nx.drawing.nx_agraph(graph, filename="dependency_graph.gv")

# Print the report
print(report)
```
execution trace:
stdout:


stderr:


return code: 0