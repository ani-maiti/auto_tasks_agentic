import requests

response = requests.get('https://api.trivia.wtf/random')
if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")