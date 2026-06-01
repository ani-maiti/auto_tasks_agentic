import feedparser

print("Parsing the RSS feed...")
feed = feedparser.parse('cnet_rss.xml')
entries = feed.entries[:50]

print(f"Retrieved {len(entries)} articles.")