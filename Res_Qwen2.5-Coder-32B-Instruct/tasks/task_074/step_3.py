import json
import requests

print("Fetching top 5 story IDs...")
response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_story_ids = response.json()[:5]
print(top_story_ids)