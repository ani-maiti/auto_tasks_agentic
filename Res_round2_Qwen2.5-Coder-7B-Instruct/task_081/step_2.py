import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = []
for i, item in enumerate(soup.find_all('tr', class_='athing')):
    if i >= 10:
        break
    title_tag = item.find('a', class_='storylink')
    if title_tag:
        titles.append(title_tag.get_text())

print(titles)