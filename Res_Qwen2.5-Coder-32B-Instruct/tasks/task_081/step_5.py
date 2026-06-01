import json
import requests

# Fetch the top stories IDs
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_story_ids = response.json()

# Get the titles of the top 10 stories
titles = []
for story_id in top_story_ids[:10]:
    story_response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    story_data = story_response.json()
    titles.append(story_data['title'])

print("Top 10 Hacker News Titles:")
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")