import requests

url = "https://www.wikipedia.org/robots.txt"
response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to retrieve robots.txt. Status code: {response.status_code}")