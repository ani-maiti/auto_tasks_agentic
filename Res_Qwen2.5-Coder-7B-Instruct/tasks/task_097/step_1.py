import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/programming/.rss"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')[:5]
    for item in items:
        title = item.find('title').text
        print(title)
else:
    print(f"Failed to retrieve the RSS feed. Status code: {response.status_code}")