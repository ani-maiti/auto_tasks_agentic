import requests

response = requests.get('https://api.factmonster.com/random/dog')
print(response.json())