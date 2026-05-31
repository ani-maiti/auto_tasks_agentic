import feedparser

# Ensure we have the correct feed object
feed_url = "https://techcrunch.com/feed/"  # Example tech RSS feed URL
feed = feedparser.parse(feed_url)

# Retrieve the latest fifty articles
latest_articles = feed.entries[:50]

print(f"Retrieved {len(latest_articles)} latest articles.")