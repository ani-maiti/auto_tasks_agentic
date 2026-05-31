import requests
from bs4 import BeautifulSoup

url = "https://xkcd.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
latest_comic = soup.find('div', {'id': 'comic'})
alt_text = latest_comic.find('img')['alt']
print(alt_text)