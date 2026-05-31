import requests

# Disable SSL verification to bypass the certificate error
response = requests.get('https://api.fact.nu/random', verify=False)
if response.status_code == 200:
    data = response.json()
    if 'text' in data:
        print(data['text'])
else:
    print("Failed to retrieve dog fact")