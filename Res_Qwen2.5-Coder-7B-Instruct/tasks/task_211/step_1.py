import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_titles(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = [title.get_text() for title in soup.find_all('title')]
    return titles

url = "https://example.com"  # Replace with the actual URL you want to crawl
html_content = fetch_page(url)

if html_content:
    titles = extract_titles(html_content)
    print(titles)
else:
    print("Failed to fetch the webpage.")
```

This script fetches the HTML content of the specified URL and extracts all the titles found within `<title>` tags. It then prints the list of titles. If the webpage cannot be fetched, it prints an error message.