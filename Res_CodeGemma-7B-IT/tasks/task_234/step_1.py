# Import libraries
import feedparser
import json
from collections import defaultdict

# Define the list of RSS feed URLs
rss_urls = [
    'https://rss.nytimes.com/pages/technology/index.rss',
    'https://rss.cnn.com/rss/technology.rss',
    'https://techcrunch.com/feed/',
    'https://www.theguardian.com/technology/rss',
    'https://www.bbc.com/news/technology-rss.xml'
]

# Create an empty list to store articles
articles = []

# Iterate over the RSS feed URLs
for url in rss_urls:
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Iterate over the articles in the feed
    for entry in feed.entries:
        # Create a dictionary for each article
        article = {
            'title': entry.title,
            'link': entry.link,
            'summary': entry.summary,
            'publication_date': entry.published,
            'publication_source': url
        }

        # Add the article to the list
        articles.append(article)

# Remove duplicates based on title
unique_articles = []
seen_titles = set()

for article in articles:
    if article['title'] not in seen_titles:
        unique_articles.append(article)
        seen_titles.add(article['title'])

# Save the unique articles to a JSON file
with open('technology_articles.json', 'w') as f:
    json.dump(unique_articles, f)

# Print the most common publication source
publication_counts = defaultdict(int)

for article in unique_articles:
    publication_counts[article['publication_source']] += 1

most_common_source = max(publication_counts, key=publication_counts.get)

print('Most common publication source:', most_common_source)