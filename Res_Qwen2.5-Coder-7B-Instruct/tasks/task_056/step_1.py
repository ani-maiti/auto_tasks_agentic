import requests

response = requests.get('https://xkcd.com/info.0.json')
if response.status_code == 200:
    data = response.json()
    print(data['title'])
else:
    print("Failed to fetch XKCD comic title")