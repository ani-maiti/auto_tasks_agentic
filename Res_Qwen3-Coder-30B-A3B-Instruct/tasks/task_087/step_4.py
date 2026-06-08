import requests

response = requests.get('https://python.org')
print("HTTP Headers from python.org:")
for header, value in response.headers.items():
    print(f"{header}: {value}")