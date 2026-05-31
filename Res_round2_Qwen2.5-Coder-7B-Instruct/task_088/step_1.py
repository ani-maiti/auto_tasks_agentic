import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

if response.status_code == 200:
    print("Page fetched successfully.")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
```

This code attempts to fetch the Wikipedia page for Python programming language using the `requests` library. If successful, it prints a success message; otherwise, it prints an error message with the status code.