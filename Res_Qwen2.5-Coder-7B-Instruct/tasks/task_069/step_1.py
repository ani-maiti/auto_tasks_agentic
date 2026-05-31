import requests

response = requests.get('https://api.quotable.io/random')
if response.status_code == 200:
    quote = response.json()
    print(quote['content'])
else:
    print("Failed to retrieve quote")