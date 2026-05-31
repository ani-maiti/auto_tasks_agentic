import requests

response = requests.get('http://wikipedia.org')
print(response.status_code)