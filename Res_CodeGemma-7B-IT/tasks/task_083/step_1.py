import requests

url = "https://github.com/blog"
response = requests.get(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")
latest_post_title = soup.find("a", class_="post-title").text
print(latest_post_title)