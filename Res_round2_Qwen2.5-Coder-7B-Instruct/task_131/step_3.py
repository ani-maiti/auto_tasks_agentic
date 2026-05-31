import requests

url = "https://blog.mozilla.org/"
response = requests.get(url)
print(response.status_code)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
latest_post_title = soup.find('h2', class_='entry-title').text.strip()
print(latest_post_title)