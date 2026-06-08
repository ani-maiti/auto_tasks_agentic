import requests

response = requests.head('http://example.com')
print(response.headers)