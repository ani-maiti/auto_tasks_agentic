import requests
from xml.etree import ElementTree as ET

# Fetch the RSS feed
url = "https://blog.mozilla.org/feed/"
response = requests.get(url)
feed_content = response.content

# Parse the XML
root = ET.fromstring(feed_content)

# Get the first item (latest blog post)
first_item = root.find('.//item')
title = first_item.find('title').text

print(title)