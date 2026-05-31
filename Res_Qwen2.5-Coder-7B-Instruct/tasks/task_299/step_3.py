import requests
import json

def get_page_title(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.title.string.strip() if soup.title else None
        else:
            return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

most_referenced_domain = "api.github.com"

page_title = get_page_title(most_referenced_domain)

if page_title:
    print(page_title)
else:
    print("Failed to retrieve page title.")