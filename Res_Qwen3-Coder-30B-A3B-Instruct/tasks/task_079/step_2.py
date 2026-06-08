import requests
import json

response = requests.get("https://api.github.com/repos/psf/requests")
data = response.json()
stars = data["stargazers_count"]
print(stars)