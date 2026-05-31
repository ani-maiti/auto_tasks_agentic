import requests
from bs4 import BeautifulSoup
import json

def get_linked_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def main():
    start_url = "https://en.wikipedia.org/wiki/Web_scraping"
    visited = set()
    links_to_visit = {start_url}
    link_graph = {}

    while len(visited) < 50 and links_to_visit:
        current_url = links_to_visit.pop()
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            linked_pages = get_linked_pages(current_url)
            link_graph[current_url] = linked_pages
            for page in linked_pages:
                if page.startswith('/wiki/') and page not in visited and page not in links_to_visit:
                    links_to_visit.add(page)
        except Exception as e:
            print(f"Error fetching {current_url}: {e}")

    with open('link_graph.json', 'w') as f:
        json.dump(link_graph, f, indent=2)

    # Find the page with the highest degree
    max_degree_page = max(link_graph, key=lambda k: len(link_graph[k]))
    print(f"The page with the highest degree is: {max_degree_page} with {len(link_graph[max_degree_page])} links.")

if __name__ == "__main__":
    main()
```

This script starts by defining a function `get_linked_pages` to fetch all linked pages from a given URL. The `main` function initializes the process by setting up the starting URL, a set to keep track of visited URLs, and a queue for URLs to visit. It then enters a loop where it continues to fetch and process pages until it has collected 50 unique pages. After collecting the pages, it saves the link graph to a JSON file and prints the page with the highest degree.