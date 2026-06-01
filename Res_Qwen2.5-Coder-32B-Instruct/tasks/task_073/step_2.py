import requests

top_story_id = 422  # First ID from the previous output
response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json')
story_data = response.json()
print(story_data['title'])