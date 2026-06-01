import feedparser
import json

sources = [
    "https://techcrunch.com/feed/",
    "https://www.cnet.com/rss/",
    "https://www.theverge.com/rss/index.xml",
    "https://www.wired.com/feed/rss",
    "https://www.engadget.com/rss.xml",
    "https://www.tomshardware.com/rss.xml",
    "https://www.pcworld.com/rss.xml",
    "https://www.cnn.com/business/technology/rss.xml",
    "https://www.forbes.com/technology/?format=rss",
    "https://www.bbc.com/news/technology/rss.xml"
]

articles = []

for source in sources:
    feed = feedparser.parse(source)
    for entry in feed.entries:
        article = {
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary,
            'published': entry.published,
            'source': source
        }
        articles.append(article)

print("Articles retrieved:", len(articles))