import requests

url = "https://www.python.org/sitemap.xml"
response = requests.get(url)

if response.status_code == 200:
    print("Download successful")
else:
    print(f"Failed to download, status code: {response.status_code}")

# Check if the URL is correct
print(f"URL checked: {url}")