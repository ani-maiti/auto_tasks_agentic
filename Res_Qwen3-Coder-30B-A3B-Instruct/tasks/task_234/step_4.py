# Save to JSON file
with open('technology_news.json', 'w') as f:
    json.dump(unique_articles, f, indent=2)

print("Articles saved to technology_news.json")

# Count sources and find the most common one
sources = [article['source'] for article in unique_articles]
source_counts = Counter(sources)
most_common_source = source_counts.most_common(1)[0] if source_counts else None

print(f"Most common publication source: {most_common_source}")