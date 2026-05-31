# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import json
import networkx as nx

# Define the website URL
url = "https://docs.python.org/3/"

# Initialize variables
page_count = 0
graph = nx.Graph()

# Function to extract titles, headings, and internal links from a given page
def extract_page_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text.strip()
    headings = [h.text.strip() for h in soup.find_all("h1", "h2", "h3", "h4", "h5", "h6")]
    links = [a["href"] for a in soup.find_all("a", href=True) if a.text.strip()]
    return title, headings, links

# Function to build the link graph
def build_link_graph(url):
    global page_count, graph
    if page_count >= 200:
        return
    title, headings, links = extract_page_data(url)
    graph.add_node(url, title=title, headings=headings)
    for link in links:
        if link.startswith("/"):
            link = url + link
        graph.add_edge(url, link)
        page_count += 1
        build_link_graph(link)

# Function to identify hub and isolated pages
def identify_hub_and_isolated_pages():
    hub_pages = list(nx.degree_centrality(graph).items())
    hub_pages.sort(key=lambda x: x[1], reverse=True)
    hub_pages = hub_pages[:20]

    isolated_pages = list(nx.isolates(graph))

    return hub_pages, isolated_pages

# Function to save the graph to JSON
def save_graph_to_json(graph):
    with open("graph.json", "w") as f:
        json.dump(graph.nodes, f, indent=4)

# Function to generate a summary report
def generate_summary_report(hub_pages, isolated_pages):
    with open("summary_report.txt", "w") as f:
        f.write("Hub Pages:\n")
        for page, centrality in hub_pages:
            f.write(f"- {page}: {centrality}\n")

        f.write("\nIsolated Pages:\n")
        for page in isolated_pages:
            f.write(f"- {page}\n")

# Function to print the most connected page
def print_most_connected_page():
    most_connected_page = max(graph.degree, key=lambda x: x[1])
    print(f"Most Connected Page: {most_connected_page}")

# Build the link graph
build_link_graph(url)

# Identify hub and isolated pages
hub_pages, isolated_pages = identify_hub_and_isolated_pages()

# Save the graph to JSON
save_graph_to_json(graph)

# Generate a summary report
generate_summary_report(hub_pages, isolated_pages)

# Print the most connected page
print_most_connected_page()