from urllib.request import urlopen

url = "https://example.com"

with urlopen(url) as response:
    html = response.read().decode("utf-8")

print(html)