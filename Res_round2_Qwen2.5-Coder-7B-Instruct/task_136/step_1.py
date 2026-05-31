import requests

url = "https://www.wikipedia.org/sitemap.xml"
response = requests.get(url)

if response.status_code == 200:
    print("Downloaded sitemap.xml successfully.")
else:
    print(f"Failed to download sitemap.xml. Status code: {response.status_code}")