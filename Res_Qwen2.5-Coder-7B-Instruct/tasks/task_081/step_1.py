import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titles = [item.get_text() for item in soup.find_all('a', class_='storylink')]
for i, title in enumerate(titles[:10]):
    print(f"{i+1}. {title}")