import requests
import csv
from collections import Counter
import re

# Get the latest 100 story IDs from Hacker News
response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty')
story_ids = response.json()[:100]

# Fetch the stories
stories = []
for story_id in story_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
    story = story_response.json()
    if story and 'title' in story:
        stories.append(story['title'])

# Define programming languages to look for
programming_languages = [
    'Python', 'Java', 'JavaScript', 'C++', 'C#', 'C', 'Go', 'Rust', 'Swift', 'Kotlin',
    'Ruby', 'PHP', 'TypeScript', 'R', 'MATLAB', 'Scala', 'Perl', 'Haskell', 'Lua', 'Dart'
]

# Find mentions of programming languages in titles
language_mentions = []
for story in stories:
    title = story.lower()
    for lang in programming_languages:
        if lang.lower() in title:
            language_mentions.append(lang)

# Count frequencies
language_freq = Counter(language_mentions)

# Save to CSV
with open('language_frequencies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Language', 'Frequency'])
    for lang, freq in language_freq.items():
        writer.writerow([lang, freq])

print("Done")