import requests

url = "https://blog.mozilla.org/"
response = requests.get(url)
print(response.status_code)