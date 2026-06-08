from xml.etree import ElementTree as ET

# Parse the sitemap.xml file
tree = ET.parse('sitemap.xml')
root = tree.getroot()

# Count the number of URL elements
url_count = len(root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'))
print(url_count)