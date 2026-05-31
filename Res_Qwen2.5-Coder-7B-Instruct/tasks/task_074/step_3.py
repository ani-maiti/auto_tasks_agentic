import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = soup.find_all('tr', class_='athing')
top_stories = []
for i, story in enumerate(stories):
    if i >= 5:
        break
    link = story.find('a', class_='storylink')
    if link:
        top_stories.append(link.text)

for title in top_stories:
    print(title)