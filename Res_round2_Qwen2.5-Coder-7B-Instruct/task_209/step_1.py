import feedparser

# Find a public RSS feed related to technology
feed_url = "https://www.example.com/rss"  # Replace with an actual tech RSS feed URL
feed = feedparser.parse(feed_url)

print(f"Retrieved {len(feed.entries)} entries from the RSS feed.")