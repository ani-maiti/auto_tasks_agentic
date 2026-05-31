import requests

url = "https://xkcd.com/info.0.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    title = data["title"]
    print(f"The latest XKCD comic title is: {title}")
else:
    print("Failed to fetch the latest XKCD comic title.")