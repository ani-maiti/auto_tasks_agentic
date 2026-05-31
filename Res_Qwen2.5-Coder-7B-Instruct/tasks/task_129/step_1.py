import requests

response = requests.get('https://api.trivia.wtf/random')
print(response.json())