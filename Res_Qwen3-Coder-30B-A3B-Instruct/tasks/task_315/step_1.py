import requests
import json
from collections import defaultdict, Counter
import re
from urllib.parse import urlparse

# Step 1: Retrieve the latest 300 Hacker News stories
def get_top_stories(n=300):
    try:
        # Get the top story IDs
        response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
        story_ids = response.json()[:n]
        
        # Fetch details for each story
        stories = []
        for story_id in story_ids:
            story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
            story_data = story_response.json()
            if story_data and 'title' in story_data:
                stories.append(story_data)
        
        return stories
    except Exception as e:
        print(f"Error fetching stories: {e}")
        return []

# Step 2: Extract keywords and domains
def extract_keywords_and_domains(stories):
    keywords_list = []
    domains = []
    
    for story in stories:
        title = story.get('title', '')
        url = story.get('url', '')
        
        # Extract domain
        if url:
            domain = urlparse(url).netloc
            domains.append(domain)
        
        # Extract keywords (simple approach: split by spaces and remove common words)
        words = re.findall(r'\b\w+\b', title.lower())
        # Filter out common stop words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'must', 'can'}
        keywords = [word for word in words if len(word) > 2 and word not in stop_words]
        keywords_list.extend(keywords)
    
    return keywords_list, domains

# Step 3: Build keyword co-occurrence network
def build_cooccurrence_network(keywords_list):
    # Create a dictionary to store keyword connections
    cooccurrence = defaultdict(Counter)
    
    # For each keyword, find other keywords that appear in the same context
    # Here we'll consider adjacent keywords in the list as co-occurring
    for i in range(len(keywords_list) - 1):
        current_word = keywords_list[i]
        next_word = keywords_list[i + 1]
        cooccurrence[current_word][next_word] += 1
    
    # Convert to a more usable format
    edges = []
    nodes = set()
    
    for word, neighbors in cooccurrence.items():
        nodes.add(word)
        for neighbor, weight in neighbors.items():
            nodes.add(neighbor)
            edges.append({
                "source": word,
                "target": neighbor,
                "weight": weight
            })
    
    return {
        "nodes": [{"id": node} for node in nodes],
        "edges": edges
    }

# Step 4: Save graph to JSON
def save_graph_to_json(graph, filename="keyword_network.json"):
    with open(filename, 'w') as f:
        json.dump(graph, f, indent=2)

# Step 5: Generate report
def generate_report(keywords_list, domains, graph):
    keyword_counts = Counter(keywords_list)
    domain_counts = Counter(domains)
    
    report = {
        "total_keywords": len(keywords_list),
        "unique_keywords": len(keyword_counts),
        "top_keywords": keyword_counts.most_common(10),
        "total_domains": len(domains),
        "unique_domains": len(domain_counts),
        "top_domains": domain_counts.most_common(10),
        "graph_info": {
            "nodes_count": len(graph["nodes"]),
            "edges_count": len(graph["edges"])
        }
    }
    
    return report

# Execute the pipeline
stories = get_top_stories(300)
print(f"Fetched {len(stories)} stories")

keywords, domains = extract_keywords_and_domains(stories)
print(f"Extracted {len(keywords)} keywords and {len(domains)} domains")

graph = build_cooccurrence_network(keywords)
save_graph_to_json(graph)

report = generate_report(keywords, domains, graph)

# Print the most connected keyword
node_degrees = defaultdict(int)
for edge in graph["edges"]:
    node_degrees[edge["source"]] += edge["weight"]
    node_degrees[edge["target"]] += edge["weight"]

most_connected_keyword = max(node_degrees, key=node_degrees.get)
print(f"Most connected keyword: {most_connected_keyword}")