import xml.etree.ElementTree as ET

tree = ET.parse('sitemap-index.xml')
root = tree.getroot()

sitemaps = [child.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text for child in root]
print(sitemaps)