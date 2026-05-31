import requests
from bs4 import BeautifulSoup
import json

# Step 2: Retrieve the latest fifty Hacker News stories
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    title_link = item.find('a', class_='storylink')
    if title_link:
        title = title_link.text.strip()
        url = title_link['href']
        stories.append({'title': title, 'url': url})

if len(stories) == 0:
    print("Failed to retrieve stories. Trying again...")
else:
    print(f"Retrieved {len(stories)} stories.")