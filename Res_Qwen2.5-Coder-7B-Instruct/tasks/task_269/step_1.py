import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Retrieve the latest one hundred stories from Hacker News
url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = []
for item in soup.find_all('tr', class_='athing'):
    title = item.find('a', class_='storylink').text
    link = item.find('a', class_='storylink')['href']
    if link.startswith('//'):
        link = 'https:' + link
    stories.append((title, link))

print(f"Retrieved {len(stories)} stories.")