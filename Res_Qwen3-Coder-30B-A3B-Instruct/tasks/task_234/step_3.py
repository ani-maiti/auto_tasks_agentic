import feedparser
import json
from collections import Counter

# Define the RSS feed URLs for technology news sources
rss_feeds = [
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://www.theguardian.com/technology/rss",
    "https://feeds.reuters.com/reuters/technologyNews",
    "https://feeds.feedburner.com/oreilly/radar",
    "https://www.wired.com/feed/rss"
]

articles = []

# Parse each RSS feed
for feed_url in rss_feeds:
    try:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'source': feed.feed.title
            }
            articles.append(article)
    except Exception as e:
        print(f"Error parsing {feed_url}: {e}")

print(f"Retrieved {len(articles)} articles from RSS feeds")

# Remove duplicates by converting to tuple of title and link, then back to dict
unique_articles = []
seen = set()

for article in articles:
    # Create a hashable representation of the article
    key = (article['title'], article['link'])
    if key not in seen:
        seen.add(key)
        unique_articles.append(article)

print(f"After removing duplicates: {len(unique_articles)} unique articles")