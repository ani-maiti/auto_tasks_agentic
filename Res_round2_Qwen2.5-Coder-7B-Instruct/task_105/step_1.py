import requests

response = requests.get('https://www.python.org')
print(response.text)