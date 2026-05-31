import requests
import pandas as pd

# Define the GitHub API endpoint for searching repositories
url = "https://api.github.com/search/repositories"

# Set the parameters for the API request
params = {
    "q": "topic:<selected_topic>",
    "sort": "stars",
    "order": "desc",
    "per_page": 100,
    "page": 1
}

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the repository information
    repos = data["items"]
    
    # Create a list to store the repository details
    repo_details = []
    
    # Loop through the repositories and extract the required information
    for repo in repos:
        repo_info = {
            "name": repo["name"],
            "owner": repo["owner"]["login"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "issues": repo["open_issues_count"],
            "language": repo["language"]
        }
        repo_details.append(repo_info)
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(repo_details)
    
    # Save the DataFrame to a CSV file
    df.to_csv("github_repos.csv", index=False)
    
    # Print a success message
    print("Repository metadata retrieved and saved to github_repos.csv")
else:
    # Print an error message if the request failed
    print(f"Error: {response.status_code} - {response.text}")