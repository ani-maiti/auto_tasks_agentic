import requests

url = "https://github.com/blog"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the GitHub blog page.")
else:
    print(f"Failed to fetch the GitHub blog page. Status code: {response.status_code}")
```

This code attempts to fetch the GitHub blog page using the `requests` library. If successful, it prints a success message; otherwise, it prints an error message along with the status code.