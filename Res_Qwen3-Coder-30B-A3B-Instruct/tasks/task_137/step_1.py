import requests

response = requests.head('https://github.com')
print(response.status_code)