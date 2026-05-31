import requests
from bs4 import BeautifulSoup
import json

# Step 1: Retrieve the latest two hundred Hacker News stories
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    title_link = item.find('a', class_='storylink')
    if title_link:
        title = title_link.text.strip()
        url = title_link['href']
        if url.startswith('//'):
            url = 'http:' + url
        elif not url.startswith('http'):
            url = 'http://' + url
        domain = url.split('/')[2]
        stories.append({'title': title, 'url': url, 'domain': domain})

print(stories[:200])  # Print the first 200 stories for inspection