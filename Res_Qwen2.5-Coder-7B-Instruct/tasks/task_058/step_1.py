import requests

url = "https://www.python.org/downloads/"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
```

This code attempts to fetch the Python downloads page from python.org. If successful, it prints a success message; otherwise, it prints an error message along with the status code.