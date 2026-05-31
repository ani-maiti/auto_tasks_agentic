# Step 4: Ask for the correct organization name and retry
print("Checking organization name...")
org_name = input("Please enter the correct GitHub organization name: ")
url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100"

response = requests.get(url)
if response.status_code == 200:
    repos = response.json()
    print("Retrieved repositories successfully.")
else:
    print(f"Failed to retrieve repositories. Status code: {response.status_code}")