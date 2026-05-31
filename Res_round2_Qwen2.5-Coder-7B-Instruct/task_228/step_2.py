# Check if the API key is valid and accessible
import requests

url = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=New York"
response = requests.get(url)

if response.status_code != 200:
    print("API Key is invalid or inaccessible.")
else:
    print("API Key is valid.")