from bs4 import BeautifulSoup
import requests

# Initialize variables
visited_urls = set()
page_titles = []

# Define function to crawl a page
def crawl_page(url):
    global visited_urls, page_titles

    # Check if URL has already been visited
    if url in visited_urls:
        return

    # Add URL to visited set
    visited_urls.add(url)

    # Send GET request to the URL
    response = requests.get(url)

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract page title
    title = soup.find("title").text.strip()

    # Add title to list
    page_titles.append(title)

    # Find and crawl linked pages
    for link in soup.find_all("a", href=True):
        # Extract link URL
        link_url = link["href"]

        # Check if URL is internal
        if link_url.startswith("/") and "http" not in link_url:
            link_url = url + link_url

        # Recursively crawl internal pages
        crawl_page(link_url)

# Start crawling from homepage
crawl_page("https://www.example.com/")

# Find duplicate titles
duplicate_titles = [title for title in page_titles if page_titles.count(title) > 1]

# Generate report
print("Visited URLs:")
for url in visited_urls:
    print(url)

print("\nPage Titles:")
for title in page_titles:
    print(title)

print("\nDuplicate Titles:")
for title in duplicate_titles:
    print(title)