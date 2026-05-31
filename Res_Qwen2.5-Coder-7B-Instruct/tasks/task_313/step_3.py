import os
import glob

# Find all Markdown files in the current directory and subdirectories
markdown_files = glob.glob('**/*.md', recursive=True)

print(f"Found {len(markdown_files)} Markdown files.")

import networkx as nx

# Create a directed graph to represent the cross-reference links
graph = nx.DiGraph()

for file_path in markdown_files:
    # Read the content of the Markdown file
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Extract links from the Markdown content
    import re
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    
    # Add edges to the graph for each link
    for link in links:
        if link.endswith('.md'):
            target_file = os.path.join(os.path.dirname(file_path), link)
            if os.path.exists(target_file):
                graph.add_edge(file_path, target_file)

print("Cross-reference graph constructed.")