# Import necessary libraries
import feedparser
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.collocations import BigramCollocationFinder
import json
from collections import Counter

# Define the list of RSS feed URLs
rss_feeds = [
    'https://techcrunch.com/feed/',
    'https://www.wired.com/feed/rss',
    'https://www.arstechnica.com/feed/',
    'https://www.techradar.com/rss',
    'https://www.theverge.com/rss/technology',
    'https://techcrunch.com/feed/',
    'https://www.engadget.com/rss.xml',
    'https://www.hackernoon.com/feed',
    'https://www.reddit.com/r/technology/.rss',
    'https://medium.com/feed/technology'
]

# Create an empty list to store the article data
articles = []

# Loop through the RSS feeds and extract articles
for feed in rss_feeds:
    feed_data = feedparser.parse(feed)
    for entry in feed_data.entries:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'description': entry.description
        })

# Create a DataFrame from the article data
df = pd.DataFrame(articles)

# Remove duplicates
df = df.drop_duplicates(subset=['title', 'link', 'description'])

# Tokenize and preprocess the text
df['tokens'] = df['description'].apply(word_tokenize)
stop_words = set(stopwords.words('english'))
df['tokens'] = df['tokens'].apply(lambda tokens: [token for token in tokens if token not in stop_words])
stemmer = PorterStemmer()
df['tokens'] = df['tokens'].apply(lambda tokens: [stemmer.stem(token) for token in tokens])

# Perform part-of-speech tagging and extract nouns
df['pos_tags'] = df['tokens'].apply(pos_tag)
df['nouns'] = df['pos_tags'].apply(lambda tags: [token for token, tag in tags if tag.startswith('NN')])

# Create a Naive Bayes classifier and train it on the noun data
clf = NaiveBayesClassifier.train(
    [(nouns, 'technology') for nouns in df['nouns']],
    ['technology']
)

# Classify articles by topic
df['topic'] = df['nouns'].apply(clf.classify)

# Calculate source diversity statistics
source_counts = df['link'].value_counts()
total_articles = len(df)
unique_sources = source_counts.count()
source_diversity = unique_sources / total_articles

# Save the dataset to JSON
df.to_json('technology_dataset.json', orient='records')

# Generate a report
report = f"""
**Technology News Dataset Report**

* **Number of articles:** {total_articles}
* **Number of unique sources:** {unique_sources}
* **Source diversity:** {source_diversity:.2%}

**Most common topics:**
{Counter(df['topic']).most_common(5)}
"""

# Print the report
print(report)

# Print the most common topic
print(Counter(df['topic']).most_common(1)[0][0])