import urllib.request

url = "http://wikipedia.org/robots.txt"
response = urllib.request.urlopen(url)
data = response.read().decode('utf-8')
print(data)