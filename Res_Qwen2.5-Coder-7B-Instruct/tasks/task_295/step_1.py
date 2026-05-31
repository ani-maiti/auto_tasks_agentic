import feedparser

# List of RSS feed URLs for technology news sources
rss_feeds = [
    'https://www.cnn.com/rss/tech.rss',
    'https://www.forbes.com/sites/forbestechcouncil/feed/',
    'https://www.techcrunch.com/feed/',
    'https://www.wired.com/feed/news',
    'https://www.engadget.com/rss.xml',
    'https://www.zdnet.com/tag/technology/rss.xml',
    'https://www.tomsguide.com/rss.xml',
    'https://www.geekwire.com/feed/',
    'https://www.cnet.com/rss/news',
    'https://www.pcmag.com/rss'
]

# Fetch and parse RSS feeds
feeds_data = []
for url in rss_feeds:
    feed = feedparser.parse(url)
    feeds_data.extend(feed.entries)

print("Feeds fetched successfully.")