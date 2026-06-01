import requests

def fetch_story_details(story_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    response = requests.get(url)
    return response.json()

stories = [fetch_story_details(story_id) for story_id in top_stories]
print("Fetched details for all top 100 stories.")