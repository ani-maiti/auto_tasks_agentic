import requests

url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

response = requests.get(url)

if response.status_code == 200:
    title = response.json()["title"]
    print(title)
else:
    print("Error retrieving data")