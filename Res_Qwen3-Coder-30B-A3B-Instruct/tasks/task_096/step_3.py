import xml.etree.ElementTree as ET
import urllib.request

# Download the RSS feed
url = "https://news.ycombinator.com/rss"
with urllib.request.urlopen(url) as response:
    rss_data = response.read()

# Parse the XML
root = ET.fromstring(rss_data)

# Extract and print the first five titles
titles = []
for item in root.findall('.//item'):
    title = item.find('title')
    if title is not None:
        titles.append(title.text)
    if len(titles) == 5:
        break

# Print the titles
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")