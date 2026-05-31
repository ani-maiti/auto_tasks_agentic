import requests

url = "https://en.wikipedia.org/robots.txt"
response = requests.get(url)

print(response.text)