import requests
import json

response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
top_stories = response.json()[:100]
print("Retrieved top 100 Hacker News stories.")