import requests

url = "https://www.python.org"
response = requests.get(url)

redirect_chain = []
while response.history:
    last_redirect = response.history[-1]
    redirect_chain.append(last_redirect.url)
    response = requests.get(last_redirect.url)

for url in redirect_chain:
    print(url)