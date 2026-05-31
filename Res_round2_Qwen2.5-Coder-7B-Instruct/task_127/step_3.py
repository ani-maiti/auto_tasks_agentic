import requests

response = requests.get('https://catfact.ninja/fact')
if response.status_code == 200:
    data = response.json()
    print(data['fact'])
else:
    print(f"Failed to retrieve cat fact. Status code: {response.status_code}")