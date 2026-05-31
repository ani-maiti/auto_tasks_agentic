import requests

url = "https://www.wikipedia.org/sitemap.xml"
response = requests.get(url)

if response.status_code == 200:
    with open("sitemap.xml", "wb") as file:
        file.write(response.content)
    print("Downloaded sitemap.xml successfully.")

    # Count the number of URLs in the sitemap.xml
    import xml.etree.ElementTree as ET
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()

    urls = [elem.text for elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    print(f"Number of URLs found: {len(urls)}")
else:
    print(f"Failed to download sitemap.xml. Status code: {response.status_code}")