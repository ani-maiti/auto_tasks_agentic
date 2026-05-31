import requests

url = "https://www.python.org/sitemap.xml"
response = requests.get(url)

print(len(response.text.split()))