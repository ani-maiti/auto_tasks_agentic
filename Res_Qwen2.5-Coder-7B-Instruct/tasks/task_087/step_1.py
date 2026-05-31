import requests

response = requests.get('http://python.org')
print(response.headers)