import requests

url = "https://api.github.com/repos/requests/requests"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    contributors = data["contributors_url"]
    contributors_response = requests.get(contributors)
    contributors_data = contributors_response.json()
    num_contributors = len(contributors_data)
    print(num_contributors)
else:
    print("Error retrieving data")