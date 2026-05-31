import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = soup.find_all('tr', class_='athing')
if len(stories) >= 5:
    top_stories = [story.find('a', class_='storylink').text for story in stories[:5]]
else:
    top_stories = [story.find('a', class_='storylink').text for story in stories]

for title in top_stories:
    print(title)