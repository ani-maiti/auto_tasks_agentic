from feedparser import parse

feed = parse("https://news.ycombinator.com/rss")

for item in feed.entries[:5]:
    print(item.title)

print(feed.entries[0].link)
```
execution trace:
stdout:
Microsoft degrades functionality of perpetually-licensed offline products
Domain expertise has always been the real moat
Shantell Sans (2023)
Racket v9.2 is now available
I found a seashell in the middle of the desert
https://news.ycombinator.com/item?id=38073826


stderr:


return code: 0