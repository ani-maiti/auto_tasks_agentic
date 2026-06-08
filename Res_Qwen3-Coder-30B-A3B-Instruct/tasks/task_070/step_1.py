import requests
from bs4 import BeautifulSoup

url = "https://apod.nasa.gov/apod/astropix.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the title in the page
title_tag = soup.find('b')
if title_tag:
    title = title_tag.get_text().strip()
    print(title)
else:
    # If no bold tag found, try to find title in meta tags or other common locations
    title = soup.find('meta', attrs={'name': 'description'})
    if title:
        print(title['content'])
    else:
        print("Title not found")