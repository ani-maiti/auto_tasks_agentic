import requests
from bs4 import BeautifulSoup

url = "https://blog.mozilla.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

latest_post_title = soup.find('h2', class_='entry-title').text.strip()
print(latest_post_title)