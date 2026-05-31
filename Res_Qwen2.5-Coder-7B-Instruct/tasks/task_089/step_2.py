import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Linux"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Check if the title element exists before trying to extract its text
title_tag = soup.find('h1', class_='firstHeading')
if title_tag:
    title = title_tag.text
else:
    title = "Title not found"

print(title)