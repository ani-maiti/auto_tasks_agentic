import feedparser
import json
from collections import defaultdict

# Define the RSS feed URL
rss_url = "https://techcrunch.com/feed/"

# Retrieve the RSS feed
feed = feedparser.parse(rss_url)

# Extract article titles and categorize them by keyword
categories = defaultdict(list)
for entry in feed.entries:
    title = entry.title
    for keyword in ["AI", "machine learning", "technology", "software", "hardware", "cybersecurity", "cloud computing"]:
        if keyword.lower() in title.lower():
            categories[keyword].append(title)

# Generate statistics
statistics = {
    "total_articles": len(feed.entries),
    "categories": {
        category: len(titles)
        for category, titles in categories.items()
    },
}

# Save the dataset to JSON
with open("tech_news_dataset.json", "w") as f:
    json.dump(statistics, f)

# Print success message
print("Dataset saved successfully!")