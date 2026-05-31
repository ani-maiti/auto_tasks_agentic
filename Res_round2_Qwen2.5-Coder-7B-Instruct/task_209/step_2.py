import feedparser

# Try another public RSS feed related to technology
feed_url = "https://techcrunch.com/feed/"  # Example tech RSS feed URL
feed = feedparser.parse(feed_url)

print(f"Retrieved {len(feed.entries)} entries from the RSS feed.")