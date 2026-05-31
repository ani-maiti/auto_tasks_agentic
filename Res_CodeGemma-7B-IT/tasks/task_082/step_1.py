import requests

url = "https://realpython.com/blog/feed/"
response = requests.get(url)

from xml.etree import ElementTree as ET

root = ET.fromstring(response.content)

latest_post = root.find("item")
latest_title = latest_post.find("title").text

print(latest_title)