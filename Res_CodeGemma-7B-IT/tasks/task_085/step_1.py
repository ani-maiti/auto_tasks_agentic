import requests

response = requests.get("https://github.com/robots.txt")

if response.status_code == 200:
    print(response.text)
else:
    print("Error fetching robots.txt:", response.status_code)