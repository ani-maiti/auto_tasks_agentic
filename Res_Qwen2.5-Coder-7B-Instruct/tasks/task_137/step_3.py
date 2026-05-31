import requests

response = requests.get('https://github.com')
print("HTTP status code for github.com:", response.status_code)