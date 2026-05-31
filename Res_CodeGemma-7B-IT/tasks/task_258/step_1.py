import requests
from bs4 import BeautifulSoup
import json

# Get the top 100 GitHub repositories tagged with data-science
url = "https://github.com/topics/data-science?l=python"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extract repository information
repositories = []
for repo in soup.find_all("a", class_="v-align-middle lh-3 flex-grow-1 min-width-0"):
    name = repo.text.strip()
    language = repo.find("span", class_="repo-language").text.strip()
    repositories.append({"name": name, "language": language})

# Classify repositories by language
language_counts = {}
for repo in repositories:
    language = repo["language"]
    language_counts[language] = language_counts.get(language, 0) + 1

# Save results to JSON
with open("repositories.json", "w") as f:
    json.dump(repositories, f)

# Print language statistics
print("Language Statistics:")
for language, count in language_counts.items():
    print(f"{language}: {count}")