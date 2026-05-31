import requests

# Disable SSL verification for demonstration purposes
response = requests.get('https://api.quotable.io/random', verify=False)
if response.status_code == 200:
    quote = response.json()
    print(quote['content'])
else:
    print("Failed to retrieve quote")