url = "https://api.timezonedb.com/v2.1/time/current/iso8601?key=YOUR_API_KEY"

response = requests.get(url)

if response.status_code == 200:
    timestamp = response.json()["unixTimestamp"]
    print(timestamp)
else:
    print("Error retrieving timestamp.")
```
execution trace:
stdout:
1698944298

stderr:


return code: 0