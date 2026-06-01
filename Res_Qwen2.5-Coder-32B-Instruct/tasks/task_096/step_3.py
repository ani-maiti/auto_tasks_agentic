import feedparser

url = "https://news.ycombinator.com/rss"
feed = feedparser.parse(url)

for i, entry in enumerate(feed.entries):
    if i < 5:
        print(entry.title)