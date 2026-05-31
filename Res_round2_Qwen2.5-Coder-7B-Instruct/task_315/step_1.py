import requests
from bs4 import BeautifulSoup
import json

# Step 1: Retrieve the latest three hundred Hacker News stories
def fetch_hacker_news_stories():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []
    for item in soup.find_all('tr', class_='athing'):
        title_link = item.find('a', class_='storylink')
        if title_link:
            stories.append(title_link['href'])
    return stories[:300]

stories = fetch_hacker_news_stories()
print(f"Retrieved {len(stories)} stories.")