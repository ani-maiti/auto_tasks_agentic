import requests

url = "https://api.quotable.io/random"

response = requests.get(url)

print(response.json()['content'])