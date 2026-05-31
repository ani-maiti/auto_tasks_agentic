import requests

url = "https://openai.com/"

def get_redirect_chain(url):
  redirects = []
  response = requests.get(url)
  while response.history:
    redirects.append(response.url)
    response = response.history[-1]
  return redirects

redirects = get_redirect_chain(url)
print(redirects)