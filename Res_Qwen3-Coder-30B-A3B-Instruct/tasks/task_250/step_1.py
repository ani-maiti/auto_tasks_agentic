import requests
import csv
from urllib.parse import urlparse
from collections import Counter

# Get the latest 100 story IDs from Hacker News
response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
story_ids = response.json()[:100]

# Fetch the stories
stories = []
for story_id in story_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
    story = story_response.json()
    if story and 'url' in story and story['url']:
        stories.append(story)

# Extract domains from URLs
domains = []
for story in stories:
    try:
        parsed_url = urlparse(story['url'])
        domains.append(parsed_url.netloc)
    except Exception as e:
        continue

# Count domain frequencies
domain_counts = Counter(domains)

# Save to CSV
with open('hacker_news_domains.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Domain', 'Count'])
    for domain, count in domain_counts.most_common():
        writer.writerow([domain, count])

# Print top 20 domains
top_20 = domain_counts.most_common(20)
for i, (domain, count) in enumerate(top_20, 1):
    print(f"{i:2d}. {domain:<40} ({count})")