import requests

response = requests.get("https://www.python.org")

for header, value in response.headers.items():
    print(f"{header}: {value}")