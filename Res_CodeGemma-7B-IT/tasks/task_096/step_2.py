from feedparser import parse

feed = parse("https://news.ycombinator.com/rss")

for item in feed.entries[:5]:
    print(item.title)