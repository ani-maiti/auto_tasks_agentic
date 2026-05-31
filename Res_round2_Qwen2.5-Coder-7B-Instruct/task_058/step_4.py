import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.python.org/downloads/')
soup = BeautifulSoup(response.text, 'html.parser')
latest_release = soup.find('h1', {'class': 'release-title'}).text.strip()
print(latest_release)