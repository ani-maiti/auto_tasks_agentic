# Remove duplicates by converting to tuple of title and link, then back to dict
unique_articles = []
seen = set()

for article in articles:
    # Create a hashable representation of the article
    key = (article['title'], article['link'])
    if key not in seen:
        seen.add(key)
        unique_articles.append(article)

print(f"After removing duplicates: {len(unique_articles)} unique articles")