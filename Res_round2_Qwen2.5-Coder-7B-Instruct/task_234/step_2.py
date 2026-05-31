import json

# Load the merged articles from the JSON file
with open('merged_articles.json', 'r') as f:
    articles = json.load(f)

# Remove duplicate articles
unique_articles = []
seen_titles = set()

for article in articles:
    if article['title'] not in seen_titles:
        unique_articles.append(article)
        seen_titles.add(article['title'])

# Save the unique articles back to a JSON file
with open('unique_articles.json', 'w') as f:
    json.dump(unique_articles, f, indent=4)

print("Duplicates removed and unique articles saved to 'unique_articles.json'")