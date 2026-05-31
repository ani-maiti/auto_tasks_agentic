import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.python.org')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
print(len(links))