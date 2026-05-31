import requests

url = "http://python.org"
redirect_chain = []

while True:
    response = requests.get(url)
    if 'Location' in response.headers:
        url = response.headers['Location']
        redirect_chain.append(url)
    else:
        break

print(redirect_chain)