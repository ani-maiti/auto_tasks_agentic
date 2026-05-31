import requests

url = "https://www.python.org"
response = requests.get(url)

redirect_chain = [url]
while response.history:
    last_redirect = response.history[-1]
    redirect_chain.append(last_redirect.headers['Location'])
    response = requests.get(last_redirect.headers['Location'])

for url in redirect_chain:
    print(url)