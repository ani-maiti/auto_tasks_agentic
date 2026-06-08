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