import requests

response = requests.get('https://python.org')
headers_list = [(key, value) for key, value in response.headers.items()]
print(headers_list)