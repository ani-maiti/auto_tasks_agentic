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
    title_link = item.find('a', class_='storylink')
    if title_link:
        title = title_link.text.strip()
        url = title_link['href']
        stories.append((title, url))

# Save the titles and URLs to a CSV file
with open('hacker_news_stories.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'URL'])
    writer.writerows(stories)

print("Stories retrieved and saved to hacker_news_stories.csv")