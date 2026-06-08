import requests
import json
from datetime import datetime

# Get current date for the API request
today = datetime.now().strftime("%Y-%m-%d")

# Using the Sunrise-Sunset API
url = f"https://api.sunrise-sunset.org/json?lat=40.7128&lng=-74.0060&date={today}"

try:
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        sunrise = data['results']['sunrise']
        sunset = data['results']['sunset']
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
    else:
        print("Error retrieving data")
        
except Exception as e:
    print(f"An error occurred: {e}")