import requests

response = requests.get('https://api.chucknorris.io/jokes/random')
if response.status_code == 200:
    joke = response.json()['value']
    print(joke)
else:
    print("Failed to fetch joke")