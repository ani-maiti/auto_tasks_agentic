import requests
from urllib.parse import urlparse

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_stories = response.json()[:100]

def get_story_url(story_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json')
    story = response.json()
    return story.get('url', '')

urls = [get_story_url(story_id) for story_id in top_stories]
print("Collected URLs from top 100 Hacker News stories.")