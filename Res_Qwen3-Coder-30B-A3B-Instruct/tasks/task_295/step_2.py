import feedparser
import requests
import json
from collections import Counter
from datetime import datetime

# List of technology news RSS feeds
rss_feeds = [
    "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "https://www.theguardian.com/technology/rss",
    "https://www.wired.com/feed/rss",
    "https://feeds.reuters.com/reuters/technologyNews",
    "https://www.nbcnews.com/tech/rss",
    "https://www.cnet.com/rss/news/",
    "https://www.theverge.com/rss/index.xml",
    "https://www.engadget.com/rss.xml",
    "https://arstechnica.com/feed/",
    "https://www.zdnet.com/news/rss.xml"
]

# Function to fetch articles from RSS feeds
def fetch_articles(feeds):
    all_articles = []
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries:
                article = {
                    'title': entry.title,
                    'link': entry.link,
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'published': entry.published if hasattr(entry, 'published') else '',
                    'source': feed.feed.title if hasattr(feed.feed, 'title') else feed_url
                }
                all_articles.append(article)
        except Exception as e:
            print(f"Error fetching from {feed_url}: {e}")
    return all_articles

# Fetch articles from all feeds
articles = fetch_articles(rss_feeds)
print(f"Fetched {len(articles)} articles")