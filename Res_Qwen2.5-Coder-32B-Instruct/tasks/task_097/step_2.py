import xml.etree.ElementTree as ET

tree = ET.parse('reddit_programming.rss')
root = tree.getroot()

namespace = {'ns': 'http://www.w3.org/2005/Atom'}
items = root.findall('.//ns:entry', namespace)

for i, item in enumerate(items[:5]):
    title = item.find('ns:title', namespace).text
    print(f"Item {i+1}: {title}")