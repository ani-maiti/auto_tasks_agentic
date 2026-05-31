import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title_tag = soup.find('h1')
if title_tag:
    print(title_tag.text.strip())
else:
    print("Title tag not found")