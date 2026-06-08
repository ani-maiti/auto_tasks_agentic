import requests

response = requests.get('https://wikipedia.org')
print(response.status_code)