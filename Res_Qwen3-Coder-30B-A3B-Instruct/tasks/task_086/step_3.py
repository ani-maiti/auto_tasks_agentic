import urllib.request

req = urllib.request.Request('http://example.com')
response = urllib.request.urlopen(req)
headers = response.headers
print("Status Code:", response.getcode())
print("Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")