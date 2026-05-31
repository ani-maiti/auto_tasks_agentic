import requests

url = "https://www.docker.com/blog"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the Docker blog page.")
else:
    print(f"Failed to retrieve the Docker blog page. Status code: {response.status_code}")
```

This code attempts to fetch the Docker blog page using the `requests` library. If successful, it prints a success message; otherwise, it prints an error message along with the status code.