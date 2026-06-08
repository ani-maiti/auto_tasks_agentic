# Create a graph representation
graph = defaultdict(set)

# Pattern to match markdown links
link_pattern = r'\[.*?\]\((.*?)\)'

for file_path in markdown_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all links in the file
    links = re.findall(link_pattern, content)
    
    # Normalize links and add edges to graph
    for link in links:
        # Handle relative paths
        if link.startswith('./') or link.startswith('../'):
            # Convert relative path to absolute path
            base_dir = os.path.dirname(file_path)
            abs_link = os.path.normpath(os.path.join(base_dir, link))
            # Check if the linked file exists
            for md_file in markdown_files:
                if os.path.normpath(md_file) == abs_link:
                    graph[file_path].add(md_file)
                    graph[md_file].add(file_path)
                    break
        elif link.endswith('.md'):
            # Direct markdown link
            for md_file in markdown_files:
                if link in md_file:
                    graph[file_path].add(md_file)
                    graph[md_file].add(file_path)
                    break

print(f"Graph created with {len(graph)} nodes")