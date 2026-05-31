import requests

response = requests.get("https://www.python.org")

print(len(response.text.split("<a")))