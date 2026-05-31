import requests

response = requests.get("https://xkcd.com/info.0.json")

if response.status_code == 200:
    data = response.json()
    title = data["title"]
    print(f"The latest XKCD comic title is: {title}")
else:
    print("Error fetching XKCD data.")