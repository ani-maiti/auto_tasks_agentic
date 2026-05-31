import re

# Define keyword categories for classification
categories = {
    "AI": ["artificial intelligence", "machine learning"],
    "Blockchain": ["blockchain", "cryptocurrency"],
    "Cybersecurity": ["cybersecurity", "hacking"],
    "Data Science": ["data science", "big data"]
}

# Classify titles by keyword category
classified_articles = {}

for article in latest_articles:
    title = article.title.lower()
    category = None
    
    for cat_name, keywords in categories.items():
        if any(keyword in title for keyword in keywords):
            category = cat_name
            break
    
    if category:
        if category not in classified_articles:
            classified_articles[category] = []
        classified_articles[category].append(article)

print("Articles classified by category:")
for category, articles in classified_articles.items():
    print(f"{category}: {len(articles)} articles")