import requests

url = "https://www.openstreetmap.org/"
response = requests.get(url)

if response.status_code == 200:
    print("Download successful")
else:
    print(f"Failed to download, status code: {response.status_code}")