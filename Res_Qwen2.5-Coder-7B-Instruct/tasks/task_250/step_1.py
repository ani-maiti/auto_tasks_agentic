import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import csv

# Step 1: Retrieve the latest one hundred Hacker News stories
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    link = item.find('a', class_='storylink')
    if link:
        href = link['href']
        if not href.startswith('item?id='):
            stories.append(href)

# Limit to the latest 100 stories
stories = stories[:100]

print(f"Retrieved {len(stories)} stories.")