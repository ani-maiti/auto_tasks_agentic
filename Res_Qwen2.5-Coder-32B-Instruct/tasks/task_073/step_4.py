import requests

# Fetch the top story ID again
top_story_ids_response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_story_ids = top_story_ids_response.json()

# Get the first story ID
top_story_id = top_story_ids[0]

# Fetch the story details
response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{top_story_id}.json')
story_data = response.json()
print(story_data['title'])