# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the topic and number of repositories to retrieve
topic = "python"
num_repos = 100

# Create an empty list to store repository data
repo_data = []

# Function to extract repository information
def extract_repo_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract repository name and owner
    repo_name = soup.find("h1", class_="h3 lh-condensed").text.split("/")[1]
    repo_owner = soup.find("h1", class_="h3 lh-condensed").text.split("/")[0]

    # Extract stars, forks, and issues
    stars = int(soup.find("a", class_="social-count js-social-count").text.replace(",", ""))
    forks = int(soup.find("a", class_="social-count js-social-count").next_sibling.next_sibling.text.replace(",", ""))
    issues = int(soup.find("a", class_="social-count js-social-count").next_sibling.next_sibling.next_sibling.next_sibling.text.replace(",", ""))

    # Extract language information
    language = soup.find("span", class_="repo-lang").text.strip()

    return repo_name, repo_owner, stars, forks, issues, language

# Loop through the top repositories
for i in range(num_repos):
    # Construct the repository URL
    url = f"https://github.com/topics/{topic}?l={i+1}"

    # Extract repository information
    repo_name, repo_owner, stars, forks, issues, language = extract_repo_info(url)

    # Store data in the list
    repo_data.append([repo_name, repo_owner, stars, forks, issues, language])

# Create a DataFrame from the data
df = pd.DataFrame(repo_data, columns=["repo_name", "repo_owner", "stars", "forks", "issues", "language"])

# Save the DataFrame to a CSV file
df.to_csv("github_topic_data.csv", index=False)

# Print the most dominant language
print(df["language"].value_counts().head(1))