import requests

response = requests.get("https://api.github.com/repos/requests/requests")
print(response.json()["stargazers_count"])