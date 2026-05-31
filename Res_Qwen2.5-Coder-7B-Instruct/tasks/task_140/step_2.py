import requests

url = "https://www.python.org"
response = requests.get(url)

for resp in response.history:
    print(f"Redirected from {resp.url} to {resp.headers['Location']}")