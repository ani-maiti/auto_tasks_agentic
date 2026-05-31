import requests

response = requests.get("https://www.wikipedia.org")

print(response.headers['Content-Type'])
```
execution trace:
stdout:
text/html; charset=UTF-8


stderr:


return code: 0