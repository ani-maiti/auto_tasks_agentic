import requests
from bs4 import BeautifulSoup
import json

# Step 1: Retrieve the latest fifty Hacker News stories
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    title_tag = item.find('a', class_='storylink')
    if title_tag:
        title = title_tag.get_text()
        url = title_tag['href']
        stories.append({'title': title, 'url': url})

print(f"Retrieved {len(stories)} stories.")