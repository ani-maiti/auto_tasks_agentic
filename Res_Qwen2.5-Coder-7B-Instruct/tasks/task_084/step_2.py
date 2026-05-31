import urllib.request

url = "https://www.wikipedia.org/robots.txt"
try:
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f"Failed to retrieve robots.txt. Error: {e.code} {e.reason}")