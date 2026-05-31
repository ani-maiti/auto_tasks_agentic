from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

def crawl_wiki(start_page):
    visited = set()
    graph = {}

    def visit(page):
        if page in visited:
            return
        visited.add(page)

        response = urlopen(f"https://en.wikipedia.org/wiki/{page}")
        soup = BeautifulSoup(response.read(), "html.parser")

        links = [a.text for a in soup.find_all("a", href=True) if a.text.strip() and not a.text.startswith("Help:")]

        graph[page] = links
        for link in links:
            visit(link)

    visit(start_page)

    return graph

def find_page_with_highest_degree(graph):
    degrees = {page: len(links) for page, links in graph.items()}
    return max(degrees, key=degrees.get)

graph = crawl_wiki("Python")
json.dump(graph, open("graph.json", "w"))

page_with_highest_degree = find_page_with_highest_degree(graph)

print(page_with_highest_degree)