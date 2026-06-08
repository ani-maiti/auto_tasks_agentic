import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()
print(data["fact"])