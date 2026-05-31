import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stories = soup.find_all('tr', class_='athing')
top_stories = [story.find('a', class_='storylink').text for story in stories[:5]]

for title in top_stories:
    print(title)