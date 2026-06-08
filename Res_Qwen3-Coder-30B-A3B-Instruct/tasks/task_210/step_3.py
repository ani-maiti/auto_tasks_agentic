import requests
import json
from collections import Counter

# Retrieve the latest 50 Hacker News story IDs
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
story_ids = response.json()[:50]

# Fetch details for each story
stories = []
for story_id in story_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
    story_data = story_response.json()
    if story_data and 'title' in story_data and 'url' in story_data:
        stories.append({
            'title': story_data['title'],
            'url': story_data['url']
        })

# Define topic keywords
tech_keywords = ['tech', 'technology', 'software', 'programming', 'developer', 'code', 'ai', 'machine learning', 'data science']
science_keywords = ['science', 'research', 'study', 'discover', 'innovation', 'experiment']
business_keywords = ['business', 'startup', 'company', 'market', 'finance', 'economy', 'entrepreneur']
security_keywords = ['security', 'hack', 'cyber', 'privacy', 'encryption', 'vulnerability']

# Classify stories
classified_stories = []
for story in stories:
    title = story['title'].lower()
    categories = []
    
    if any(keyword in title for keyword in tech_keywords):
        categories.append('Technology')
    if any(keyword in title for keyword in science_keywords):
        categories.append('Science')
    if any(keyword in title for keyword in business_keywords):
        categories.append('Business')
    if any(keyword in title for keyword in security_keywords):
        categories.append('Security')
        
    classified_stories.append({
        'title': story['title'],
        'url': story['url'],
        'categories': categories if categories else ['General']
    })

# Compute category frequencies
all_categories = [category for story in classified_stories for category in story['categories']]
category_counts = Counter(all_categories)

# Save to JSON
with open('hacker_news_classification.json', 'w') as f:
    json.dump(classified_stories, f, indent=2)

# Print dominant category
dominant_category = category_counts.most_common(1)[0][0] if category_counts else 'None'
print(dominant_category)

# Print all stories with their categories for verification
for story in classified_stories:
    print(f"Title: {story['title']}")
    print(f"Categories: {', '.join(story['categories'])}")
    print(f"URL: {story['url']}\n")