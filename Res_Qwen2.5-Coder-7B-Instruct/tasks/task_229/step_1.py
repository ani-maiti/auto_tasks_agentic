import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Retrieve the latest one hundred Hacker News stories
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
            url = "https:" + url
        stories.append((title, url))

print(f"Retrieved {len(stories)} stories.")
```

This code retrieves the latest one hundred Hacker News stories and prints out how many stories were retrieved. The next step would be to extract company names from these stories.