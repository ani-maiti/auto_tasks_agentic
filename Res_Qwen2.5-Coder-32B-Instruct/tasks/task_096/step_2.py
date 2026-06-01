import xml.etree.ElementTree as ET
import requests

url = "https://news.ycombinator.com/rss"
response = requests.get(url)
root = ET.fromstring(response.content)

for i, item in enumerate(root.findall('.//item')):
    if i < 5:
        title = item.find('title').text
        print(title)