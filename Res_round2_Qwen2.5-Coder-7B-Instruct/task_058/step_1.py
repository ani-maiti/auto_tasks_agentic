import requests

response = requests.get('https://www.python.org/downloads/')
print(response.text)