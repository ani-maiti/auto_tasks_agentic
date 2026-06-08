import requests

response = requests.head('https://python.org')
print(response.headers)