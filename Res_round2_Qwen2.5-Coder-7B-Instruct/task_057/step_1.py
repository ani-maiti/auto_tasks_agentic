import requests

url = "https://xkcd.com/info.0.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    alt_text = data["alt"]
    print(alt_text)
else:
    print(f"Failed to retrieve XKCD comic. Status code: {response.status_code}")