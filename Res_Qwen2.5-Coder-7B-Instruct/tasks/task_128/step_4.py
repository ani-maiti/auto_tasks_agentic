import requests

response = requests.get('https://catfact.ninja/fact')
print(response.json())