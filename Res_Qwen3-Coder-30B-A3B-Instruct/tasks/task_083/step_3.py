import feedparser

# Parse the RSS feed
feed = feedparser.parse('https://github.blog/feed/')

# Get the latest post title
latest_title = feed.entries[0].title
print(latest_title)