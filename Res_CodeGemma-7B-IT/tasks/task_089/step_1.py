import requests

response = requests.get("https://en.wikipedia.org/api/rest_v1/page/linux")

if response.status_code == 200:
    title = response.json()["query"]["pages"][0]["title"]
    print(title)
else:
    print("Error fetching page title.")