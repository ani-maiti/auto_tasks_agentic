import requests

url = "https://api.github.com/repos/canonical/ubuntu-releases/latest"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["tag_name"])
else:
    print("Error retrieving data")
```
execution trace:
stdout:
23.04


stderr:


return code: 0