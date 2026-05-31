import requests
from bs4 import BeautifulSoup

url = "https://www.openstreetmap.org/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string
    print(title)
else:
    print(f"Failed to download, status code: {response.status_code}")