# Remove duplicates based on title and link
unique_articles = []
seen = set()

for article in articles:
    # Create a unique identifier for each article
    identifier = (article['title'], article['link'])
    if identifier not in seen:
        seen.add(identifier)
        unique_articles.append(article)

print(f"After removing duplicates: {len(unique_articles)} articles")