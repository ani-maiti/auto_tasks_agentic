import feedparser
rss_url = "https://www.reddit.com/r/programming/.rss"
feed = feedparser.parse(rss_url)
for i in range(5):
    print(feed.entries[i].title)