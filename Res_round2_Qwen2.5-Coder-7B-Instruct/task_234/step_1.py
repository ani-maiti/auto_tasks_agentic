import feedparser

# Define the URLs for the RSS feeds
feed_urls = [
    "https://www.cnn.com/rss/tech.rss",
    "https://www.techcrunch.com/feed/",
    "https://www.wired.com/feed/news",
    "https://www.engadget.com/rss",
    "https://www.forbes.com/sites/forbestechcouncil/feed/"
]

# Initialize an empty list to store all articles
all_articles = []

# Loop through each feed URL and parse it
for url in feed_urls:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        all_articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary if hasattr(entry, 'summary') else ''
        })

# Save the merged articles to a JSON file
import json
with open('merged_articles.json', 'w') as f:
    json.dump(all_articles, f, indent=4)

print("RSS feeds retrieved and merged into 'merged_articles.json'")