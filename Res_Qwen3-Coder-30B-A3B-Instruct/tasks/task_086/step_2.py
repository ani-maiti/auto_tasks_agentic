import requests

response = requests.get('http://example.com')
print("Status Code:", response.status_code)
print("Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")