import requests

response = requests.get('https://python.org')
print("Status Code:", response.status_code)
print("Headers:")
for key, value in response.headers.items():
    print(f"{key}: {value}")