import requests

url = "https://en.wikipedia.org/api/rest_v1/page/Python_(programming_language)"

response = requests.get(url)

if response.status_code == 200:
    title = response.json()["query"]["pages"][0]["title"]
    print(title)
else:
    print("Error fetching page title")