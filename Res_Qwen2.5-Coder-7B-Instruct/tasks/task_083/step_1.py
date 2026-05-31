import requests

url = "https://github.com/blog"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the GitHub blog page.")
else:
    print(f"Failed to retrieve the GitHub blog page. Status code: {response.status_code}")