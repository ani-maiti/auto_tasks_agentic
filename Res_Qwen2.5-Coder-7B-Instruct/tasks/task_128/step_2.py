import requests

response = requests.get('https://dog-api.kindacode.com/facts/')
print(response.json())