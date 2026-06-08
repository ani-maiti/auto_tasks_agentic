import urllib.request

url = "https://wikipedia.org/robots.txt"
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')
print(content)