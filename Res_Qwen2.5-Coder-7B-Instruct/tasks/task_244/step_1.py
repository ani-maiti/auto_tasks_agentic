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
    queue = [start_url]
    link_graph = {}

    while len(visited) < 50 and queue:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)

        try:
            linked_pages = get_linked_pages(url)
            for link in linked_pages:
                if link.startswith('/wiki/') and ':' not in link:
                    full_link = f"https://en.wikipedia.org{link}"
                    if full_link not in visited:
                        queue.append(full_link)
                        link_graph[url] = link_graph.get(url, []) + [full_link]
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    with open('link_graph.json', 'w') as f:
        json.dump(link_graph, f, indent=2)

    # Find the page with the highest degree
    max_degree_page = max(link_graph, key=lambda k: len(link_graph[k]))
    print(f"The page with the highest degree is: {max_degree_page} with {len(link_graph[max_degree_page])} links.")

if __name__ == "__main__":
    main()
```

This script starts by defining a function `get_linked_pages` to fetch all linked pages from a given URL. The `main` function initializes a queue with the starting URL and iterates until 50 unique pages are collected. It uses a set `visited` to keep track of already processed URLs and a list `queue` to manage the pages to be processed. The script then saves the link graph to a JSON file and identifies the page with the highest number of outgoing links.