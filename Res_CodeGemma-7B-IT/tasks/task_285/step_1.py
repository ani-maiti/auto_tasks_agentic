# Import libraries
import requests
from bs4 import BeautifulSoup
import json
import datetime
from collections import defaultdict

# Define URL and parameters
url = "https://news.ycombinator.com/"
params = {"from": "new"}

# Make request and parse HTML
response = requests.get(url, params=params)
soup = BeautifulSoup(response.content, "html.parser")

# Extract story information
stories = []
for story in soup.find_all("tr", class_="athing comhead"):
    title = story.find("a", class_="storylink").text.strip()
    domain = story.find("a", class_="domain").text.strip()
    score = int(story.find("span", class_="score").text.strip())
    stories.append({"title": title, "domain": domain, "score": score})

# Classify stories into categories
categories = defaultdict(list)
for story in stories:
    categories[story["domain"]].append(story)

# Compute category statistics
category_stats = {}
for category, stories in categories.items():
    num_stories = len(stories)
    avg_score = sum([story["score"] for story in stories]) / num_stories
    category_stats[category] = {"num_stories": num_stories, "avg_score": avg_score}

# Save dataset to JSON
filename = f"hacker_news_{datetime.datetime.now().strftime('%Y-%m-%d')}.json"
with open(filename, "w") as f:
    json.dump(stories, f)

# Generate report
print("Hacker News Report")
for category, stats in category_stats.items():
    print(f"{category}: {stats['num_stories']} stories, average score: {stats['avg_score']}")

# Print fastest growing category
fastest_growing_category = max(category_stats, key=lambda category: category_stats[category]["num_stories"])
print(f"Fastest Growing Category: {fastest_growing_category}")