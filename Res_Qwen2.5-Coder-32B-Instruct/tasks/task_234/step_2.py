import feedparser
import pandas as pd
from collections import Counter

# Define RSS feed URLs
rss_feeds = [
    "https://techcrunch.com/feed/",
    "https://www.cnet.com/rss/",
    "https://www.theverge.com/rss/index.xml",
    "https://www.wired.com/feed/rss",
    "https://www.tomshardware.com/rss.xml"
]

# Initialize a list to store articles
articles = []

# Fetch and parse each RSS feed
for url in rss_feeds:
    feed = feedparser.parse(url)
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'source': feed.feed.title
        }
        articles.append(article)

# Convert list to DataFrame
df = pd.DataFrame(articles)

# Remove duplicates based on title and link
df.drop_duplicates(subset=['title', 'link'], inplace=True)

# Save to JSON
df.to_json('merged_articles.json', orient='records', lines=True)

# Print the most common publication source
most_common_source = df['source'].value_counts().idxmax()
print(f"Most common publication source: {most_common_source}")