import feedparser

# Download the RSS feed for Reddit programming
feed = feedparser.parse('https://www.reddit.com/r/programming/.rss')

# Print the first five item titles
for i, entry in enumerate(feed.entries[:5]):
    print(entry.title)