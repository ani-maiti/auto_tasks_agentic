import requests

response = requests.get("https://www.wikipedia.org")

print(response.headers['Content-Type'])

if response.status_code == 200:
    print("Wikipedia is online.")
else:
    print("Wikipedia is not online.")
```
execution trace:
stdout:
text/html; charset=UTF-8
Wikipedia is online.


stderr:


return code: 0