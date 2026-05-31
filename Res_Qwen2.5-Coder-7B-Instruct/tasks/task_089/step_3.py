import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Linux"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title from the HTML
title_tag = soup.find('title')
if title_tag:
    title = title_tag.text.split(' - ')[0]
else:
    title = "Title not found"

print(title)