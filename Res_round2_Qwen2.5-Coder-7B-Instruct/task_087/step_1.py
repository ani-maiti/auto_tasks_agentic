import requests

response = requests.get('https://www.python.org')
headers = response.headers
print(headers)