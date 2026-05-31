import feedparser

urls = [
    'https://www.cnn.com/rss/cnn_latest.rss',
    'https://techcrunch.com/feed/',
    'https://www.engadget.com/rss.xml',
    'https://www.wired.com/feed/news',
    'https://www.forbes.com/sites/forbestechcouncil/rss'
]

feeds = [feedparser.parse(url) for url in urls]
print("Feeds retrieved successfully.")