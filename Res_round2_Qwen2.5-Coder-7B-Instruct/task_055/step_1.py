import requests

response = requests.get('https://api.github.com')
if response.status_code == 200:
    print(response.json()['updated_at'])
else:
    print("Failed to retrieve data")