import json
from collections import Counter

# Load the unique articles from the JSON file
with open('unique_articles.json', 'r') as f:
    articles = json.load(f)

# Extract the publication sources
sources = [article['link'].split('/')[2] for article in articles]

# Count the occurrences of each source
source_counts = Counter(sources)

# Find the most common source
most_common_source = source_counts.most_common(1)[0][0]

print(f"The most common publication source is: {most_common_source}")