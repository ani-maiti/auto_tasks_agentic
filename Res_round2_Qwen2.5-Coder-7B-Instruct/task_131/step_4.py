import requests

url = "https://blog.mozilla.org/"
response = requests.get(url)
print(response.status_code)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
latest_post_title = soup.find('h2', class_='post-title').text.strip() if soup.find('h2', class_='post-title') else "Title not found"
print(latest_post_title)