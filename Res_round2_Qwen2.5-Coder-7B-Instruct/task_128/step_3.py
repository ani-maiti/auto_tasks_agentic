import requests

# Verify the SSL certificate properly
response = requests.get('https://api.fact.nu/random', verify=True)
if response.status_code == 200:
    data = response.json()
    if 'text' in data:
        print(data['text'])
else:
    print("Failed to retrieve dog fact")