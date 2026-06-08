import requests
import json

# Fetch the top stories from Hacker News API
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
top_story_ids = response.json()

# Get the first 5 story IDs
top_5_ids = top_story_ids[:5]

# Fetch details for each of the top 5 stories
titles = []
for story_id in top_5_ids:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty')
    story_data = story_response.json()
    titles.append(story_data['title'])

# Print the titles
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")