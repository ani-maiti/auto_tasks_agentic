organization = input("Enter the correct GitHub organization name: ")
url = f"https://api.github.com/orgs/{organization}/repos"
response = requests.get(url)

if response.status_code == 200:
    repos = response.json()
    repo_names = [repo['name'] for repo in repos]
    print(f"Retrieved {len(repo_names)} repositories.")
else:
    print("Failed to retrieve repositories.")
    exit(1)