import requests

response = requests.get('https://python.org')
headers_dict = dict(response.headers)
print(headers_dict)