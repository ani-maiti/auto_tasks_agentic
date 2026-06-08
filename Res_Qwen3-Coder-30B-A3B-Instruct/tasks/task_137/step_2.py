import requests

response = requests.get('https://github.com')
print(f"Status Code: {response.status_code}")
print(f"Response Headers: {dict(response.headers)}")