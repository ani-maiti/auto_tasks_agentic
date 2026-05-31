import requests

response = requests.get('https://api.unixtimestamp.com/')
print(response.text)