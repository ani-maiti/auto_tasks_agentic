import requests
import json

def fetch_hacker_news_stories():
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url)
    top_story_ids = response.json()[:200]
    stories = []
    for story_id in top_story_ids:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        story_data = story_response.json()
        stories.append(story_data)
    return stories

stories = fetch_hacker_news_stories()
print("Fetched stories:", len(stories))