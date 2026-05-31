import requests

url = "https://api.github.com/repos/psf/requests"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    stars = data['stargazers_count']
    print(f"The number of stars for the requests GitHub repository is: {stars}")
else:
    print("Failed to retrieve the repository information.")
```

This script uses the `requests` library to fetch the JSON data from the GitHub API for the `psf/requests` repository. It then extracts the number of stars from the JSON response and prints it. If the request fails, it prints an error message.