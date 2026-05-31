from urllib.request import urlopen

url = "https://www.kernel.org/"
response = urlopen(url)
print(response.getheader('Content-Title'))