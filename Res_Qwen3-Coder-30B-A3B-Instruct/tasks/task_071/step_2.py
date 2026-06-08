import requests
import json
from datetime import datetime

# Get current date for the API request
current_date = datetime.now().strftime("%Y-%m-%d")

# Using the Sunrise-Sunset API to get sunrise and sunset times for London
url = f"https://api.sunrise-sunset.org/json?lat=51.5074&lng=-0.1278&date={current_date}&formatted=0"

try:
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        sunrise = data['results']['sunrise']
        sunset = data['results']['sunset']
        
        # Convert to readable format
        sunrise_time = datetime.fromisoformat(sunrise.replace('Z', '+00:00')).strftime('%H:%M:%S')
        sunset_time = datetime.fromisoformat(sunset.replace('Z', '+00:00')).strftime('%H:%M:%S')
        
        # Print the results in a more readable format
        print(f"Sunrise time for London today: {sunrise_time}")
        print(f"Sunset time for London today: {sunset_time}")
    else:
        print("Failed to retrieve data")
        
except Exception as e:
    print(f"Error occurred: {e}")