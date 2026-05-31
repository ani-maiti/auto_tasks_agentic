# Import necessary libraries
import os
import json
from collections import defaultdict

# Initialize variables
file_list = []
graph = defaultdict(list)

# Function to find Markdown files
def find_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_list.append(filename)

# Function to construct cross reference graph
def construct_graph(file_list):
    for filename in file_list:
        with open(filename, "r") as f:
            for line in f:
                for word in line.split():
                    if word.startswith("["):
                        link = word.split("|")[0].strip("[]")
                        if link in file_list:
                            graph[filename].append(link)

# Function to identify disconnected documentation groups
def identify_disconnected_groups(graph):
    visited = set()
    disconnected_groups = []

    for node in graph:
        if node not in visited:
            group = []
            dfs(node, graph, visited, group)
            disconnected_groups.append(group)

    return disconnected_groups

# Depth-first search to find connected components
def dfs(node, graph, visited, group):
    visited.add(node)
    group.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, group)

# Function to save graph to JSON
def save_graph_to_json(graph, filename):
    with open(filename, "w") as f:
        json.dump(graph, f, indent=4)

# Function to generate report
def generate_report(disconnected_groups):
    report = f"Number of disconnected documentation groups: {len(disconnected_groups)}\n"
    for group in disconnected_groups:
        report += f"Group: {', '.join(group)}\n"
    return report

# Function to print largest connected component
def print_largest_component(graph):
    visited = set()
    largest_component = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, graph, visited, component)
            largest_component.append(len(component))

    largest_component.sort(reverse=True)
    if largest_component:
        print(f"Largest connected component: {largest_component[0]}")
    else:
        print("No connected components found")

# Find Markdown files
find_markdown_files(".")

# Construct cross reference graph
construct_graph(file_list)

# Identify disconnected documentation groups
disconnected_groups = identify_disconnected_groups(graph)

# Save graph to JSON
save_graph_to_json(graph, "graph.json")

# Generate report
report = generate_report(disconnected_groups)

# Print report
print(report)

# Print largest connected component
print_largest_component(graph)