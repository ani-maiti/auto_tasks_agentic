import feedparser

# Retrieve the latest fifty articles
latest_articles = feed.entries[:50]

print(f"Retrieved {len(latest_articles)} latest articles.")