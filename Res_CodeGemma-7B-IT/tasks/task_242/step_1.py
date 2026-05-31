import requests
from bs4 import BeautifulSoup
import pandas as pd

# Retrieve top 50 starred Python repositories
response = requests.get("https://github.com/topics/python?l=python")
soup = BeautifulSoup(response.content, "html.parser")

# Extract repository information
repositories = []
for repo in soup.find_all("div", class_="Box-row"):
    repo_name = repo.find("a", class_="text-bold").text.strip()
    repo_url = repo.find("a", class_="text-bold")["href"]
    repo_stars = int(repo.find("a", class_="Link--muted").text.strip().split()[0])
    repositories.append([repo_name, repo_url, repo_stars])

# Create DataFrame and save to CSV
df = pd.DataFrame(repositories, columns=["Repository Name", "Repository URL", "Stars"])
df.to_csv("top_starred_python_repositories.csv", index=False)

# Print most common topic keyword
topic_keywords = []
for repo in repositories:
    response = requests.get(repo[1])
    soup = BeautifulSoup(response.content, "html.parser")
    for topic in soup.find_all("a", class_="topic-tag"):
        topic_keywords.append(topic.text.strip())

from collections import Counter
most_common_topic = Counter(topic_keywords).most_common(1)[0][0]
print("Most common topic keyword:", most_common_topic)