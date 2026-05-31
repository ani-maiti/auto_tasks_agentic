import requests

response = requests.get('https://www.openstreetmap.org')
print(response.text)