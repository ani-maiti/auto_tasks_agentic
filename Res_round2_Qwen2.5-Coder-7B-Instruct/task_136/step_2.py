import urllib.request

url = "https://www.wikipedia.org/sitemap.xml"
try:
    urllib.request.urlretrieve(url, "sitemap.xml")
    print("Downloaded sitemap.xml successfully.")
except Exception as e:
    print(f"Failed to download sitemap.xml: {e}")