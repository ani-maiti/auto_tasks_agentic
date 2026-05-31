import requests

response = requests.get("https://www.wikipedia.org")

print(response.status_code)