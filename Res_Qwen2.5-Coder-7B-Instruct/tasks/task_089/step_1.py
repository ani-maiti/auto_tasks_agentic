import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Linux"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1', class_='firstHeading').text
print(title)