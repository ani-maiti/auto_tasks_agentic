import requests

response = requests.get("https://en.wikipedia.org/sitemap.xml")

print(len(response.text.split()))