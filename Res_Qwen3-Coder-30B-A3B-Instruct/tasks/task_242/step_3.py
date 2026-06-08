import pandas as pd
from collections import Counter

# Read the CSV file
df = pd.read_csv("top_python_repos.csv")

# Count occurrences of each topic across all repositories
all_topics = []
for topics_str in df['topics']:
    if isinstance(topics_str, str):
        topics = [topic.strip() for topic in topics_str.split(',')]
        all_topics.extend(topics)

# Find the most common topics
topic_counter = Counter(all_topics)
most_common_topics = topic_counter.most_common(10)

print("Top 10 most common topics:")
for topic, count in most_common_topics:
    print(f"{topic}: {count}")

print(f"\nMost common topic overall: {most_common_topics[0][0]}")