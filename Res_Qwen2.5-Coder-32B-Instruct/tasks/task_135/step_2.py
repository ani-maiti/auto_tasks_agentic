import xml.etree.ElementTree as ET

tree = ET.parse('sitemap.xml')
root = tree.getroot()

url_count = 0
for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    url_count += 1

print(f"Number of URLs: {url_count}")