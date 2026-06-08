import requests

# Get the latest XKCD comic info directly
response = requests.get('https://xkcd.com/info.0.json')
data = response.json()
latest_comic_number = data['num']

# Get the specific comic data to extract the title
comic_response = requests.get(f'https://xkcd.com/{latest_comic_number}/info.0.json')
comic_data = comic_response.json()

print(comic_data['title'])