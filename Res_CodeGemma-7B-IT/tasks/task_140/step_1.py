import requests

response = requests.get('https://www.python.org')

redirects = []
while response.history:
    redirects.append(response.url)
    response = response.history[0]

print(redirects)