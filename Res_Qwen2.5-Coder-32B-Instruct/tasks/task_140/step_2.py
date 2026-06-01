import requests

url = 'http://python.org'
response = requests.get(url, allow_redirects=False)
redirect_chain = [response.url]

while response.status_code in [301, 302]:
    response = requests.get(response.headers['Location'], allow_redirects=False)
    redirect_chain.append(response.url)

print(redirect_chain)