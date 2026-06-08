import requests
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
        
        # Extract just the time part
        sunrise_time = sunrise.split('T')[1][:8]
        sunset_time = sunset.split('T')[1][:8]
        
        print(f"Sunrise: {sunrise_time}")
        print(f"Sunset: {sunset_time}")
    else:
        print("Failed to retrieve data")
        
except Exception as e:
    print(f"Error: {e}")