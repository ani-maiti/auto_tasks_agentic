import requests

url = "https://api.github.com/repos/pandas-dev/pandas/issues?state=open"
response = requests.get(url)

if response.status_code == 200:
    issues = response.json()
    print(f"Number of open issues: {len(issues)}")
else:
    print("Error retrieving issues.")