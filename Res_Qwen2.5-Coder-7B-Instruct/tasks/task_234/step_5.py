# Ensure the feeds variable is defined before this script runs
# This is a placeholder to ensure the variable is accessible
feeds = []

articles = []
for feed in feeds:
    for entry in feed.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'published': entry.published,
            'summary': entry.summary if hasattr(entry, 'summary') else None
        })

print(f"Total articles collected: {len(articles)}")