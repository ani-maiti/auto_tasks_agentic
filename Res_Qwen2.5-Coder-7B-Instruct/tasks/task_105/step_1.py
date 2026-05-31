import requests

response = requests.get('https://www.python.org')
print(response.status_code)
```

This code attempts to download the homepage of python.org and prints the HTTP status code of the response. If the request is successful, the status code should be 200.