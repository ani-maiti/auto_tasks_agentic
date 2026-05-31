import requests
from bs4 import BeautifulSoup

url = "https://apod.nasa.gov/apod/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title_tag = soup.find('h1')
if title_tag:
    title = title_tag.text.strip()
    print(f"Latest NASA Astronomy Picture of the Day Title: {title}")
else:
    print("Failed to retrieve the title.")