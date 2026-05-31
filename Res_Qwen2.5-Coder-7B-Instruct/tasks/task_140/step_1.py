import requests

url = "https://www.python.org"
response = requests.get(url)

print(response.history)