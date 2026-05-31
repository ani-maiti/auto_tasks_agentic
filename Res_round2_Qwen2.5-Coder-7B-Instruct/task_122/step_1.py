import requests

url = "https://api.github.com/repos/psf/requests/issues"
response = requests.get(url)

if response.status_code == 200:
    issues = response.json()
    open_issues_count = sum(1 for issue in issues if issue['state'] == 'open')
    print(f"Number of open issues: {open_issues_count}")
else:
    print(f"Failed to fetch issues. Status code: {response.status_code}")