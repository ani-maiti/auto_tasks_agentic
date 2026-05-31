import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.openstreetmap.org')
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.title.string
print(title)