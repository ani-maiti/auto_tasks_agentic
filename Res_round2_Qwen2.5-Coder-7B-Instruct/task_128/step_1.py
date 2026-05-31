import requests

response = requests.get('https://api.fact.nu/random')
if response.status_code == 200:
    data = response.json()
    if 'text' in data:
        print(data['text'])
else:
    print("Failed to retrieve dog fact")