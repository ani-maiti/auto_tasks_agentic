import requests

url = "https://www.python.org/downloads/"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully retrieved the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")