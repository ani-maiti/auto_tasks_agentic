import feedparser
rss_url = "https://www.reddit.com/r/programming/.rss"
feed = feedparser.parse(rss_url)
print(feed.entries[5].title)
```
execution trace:
stdout:


stderr:


return code: 0