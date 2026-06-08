import requests
import csv
from collections import Counter

# Get the top 50 most starred Python repositories
url = "https://api.github.com/search/repositories"
params = {
    "q": "language:python",
    "sort": "stars",
    "order": "desc",
    "per_page": 50
}

response = requests.get(url, params=params)
repos = response.json()["items"]

# Extract metadata and topics
repo_data = []
for repo in repos:
    repo_info = {
        "name": repo["name"],
        "full_name": repo["full_name"],
        "description": repo["description"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "url": repo["html_url"],
        "topics": repo["topics"] if "topics" in repo else []
    }
    repo_data.append(repo_info)

# Save to CSV
with open("top_python_repos.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "full_name", "description", "stars", "forks", "url", "topics"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for repo in repo_data:
        # Convert topics list to string for CSV
        repo["topics"] = ", ".join(repo["topics"])
        writer.writerow(repo)

print("Saved repository data to top_python_repos.csv")

# Classify by topic keywords
all_topics = []
for repo in repo_data:
    all_topics.extend(repo["topics"].split(", "))

# Count topic frequencies
topic_counts = Counter(all_topics)
most_common_topic = topic_counts.most_common(1)[0] if topic_counts else None

print(f"Most common topic: {most_common_topic}")