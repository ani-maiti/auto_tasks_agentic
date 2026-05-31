import requests

response = requests.get("https://www.wikipedia.org")

print(response.headers)
```
execution trace:
stdout:
{'content-type': 'text/html; charset=UTF-8', 'content-encoding': 'gzip', 'vary': 'User-Agent, Accept-Encoding', 'server': 'Apache', 'date': 'Wed, 17 May 2023 00:25:42 GMT', 'connection': 'keep-alive', 'etag': 'W/"f255f876878444003344084560458728"', 'cache-control': 'no-cache, must-revalidate', 'pragma': 'no-cache', 'expires': '-1', 'set-cookie': 'GeoIP=US:CA:Los+Angeles:34.0522:-118.2437:v4; expires=Thu, 16-May-2024 00:25:42 GMT; path=/; domain=.wikipedia.org', 'x-analytics-token': '1234567890abcdef', 'x-analytics-provider': 'Google-Analytics'}


stderr:


return code: 0