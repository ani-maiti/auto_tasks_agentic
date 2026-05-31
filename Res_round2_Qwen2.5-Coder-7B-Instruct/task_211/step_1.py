import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.find('title')
    return title_tag.string if title_tag else None

def main():
    url = input("Enter the URL of the website to crawl: ")
    visited_urls = set()
    collected_titles = {}
    
    def crawl(url):
        if url in visited_urls:
            return
        visited_urls.add(url)
        
        html = fetch_page(url)
        if html:
            title = extract_title(html)
            if title:
                if title in collected_titles:
                    collected_titles[title].append(url)
                else:
                    collected_titles[title] = [url]
                
                # Limit to 50 unique titles
                if len(collected_titles) >= 50:
                    return
                
                # Find all links and crawl them
                soup = BeautifulSoup(html, 'html.parser')
                for link in soup.find_all('a', href=True):
                    next_url = link['href']
                    if not next_url.startswith('http'):
                        next_url = f"{url}/{next_url}"
                    crawl(next_url)
    
    crawl(url)
    
    # Generate report
    duplicates = {title: urls for title, urls in collected_titles.items() if len(urls) > 1}
    print("\nDuplicate Titles Report:")
    for title, urls in duplicates.items():
        print(f"Title: {title}")
        for url in urls:
            print(f"  - {url}")

if __name__ == "__main__":
    main()
```

This script defines functions to fetch a webpage, extract the title, and recursively crawl the website starting from the given URL. It collects up to fifty unique page titles and identifies any duplicates. Finally, it generates a report listing the duplicate titles and their associated URLs.