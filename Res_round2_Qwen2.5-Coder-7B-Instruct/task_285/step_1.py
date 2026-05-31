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
        title = title_link.get_text()
        url = title_link['href']
        if not url.startswith('http'):
            url = f"https://news.ycombinator.com{url}"
        score_element = item.find_next_sibling('tr').find('span', class_='score')
        score = int(score_element.get_text().split()[0]) if score_element else 0
        stories.append({'title': title, 'url': url, 'score': score})

print(f"Retrieved {len(stories)} stories.")