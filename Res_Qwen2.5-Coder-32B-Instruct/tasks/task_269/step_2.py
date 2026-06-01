import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
response = requests.get(url)
top_stories = response.json()[:100]

print("Retrieved top 100 story IDs.")