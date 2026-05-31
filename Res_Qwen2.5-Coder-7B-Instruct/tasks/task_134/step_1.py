import requests

url = "https://kubernetes.io/blog/"
response = requests.get(url)
print(response.text)