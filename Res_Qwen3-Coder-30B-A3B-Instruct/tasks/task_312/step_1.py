import requests
import json
from datetime import datetime

# Define the city we're interested in
city = "London"

# API endpoints
weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
geo_api_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=YOUR_API_KEY"
timezone_api_url = f"http://worldtimeapi.org/api/timezone/Europe/London"

# Function to get weather data
def get_weather_data():
    try:
        response = requests.get(weather_api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Weather API error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

# Function to get geolocation data
def get_geo_data():
    try:
        response = requests.get(geo_api_url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]  # Return first result
            else:
                print("No geolocation data found")
                return None
        else:
            print(f"Geolocation API error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching geolocation data: {e}")
        return None

# Function to get timezone data
def get_timezone_data():
    try:
        response = requests.get(timezone_api_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Timezone API error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching timezone data: {e}")
        return None

# Fetch all data
weather_data = get_weather_data()
geo_data = get_geo_data()
timezone_data = get_timezone_data()

# Merge data into unified record
unified_record = {
    "city": city,
    "timestamp": datetime.now().isoformat(),
    "weather": weather_data,
    "geolocation": geo_data,
    "timezone": timezone_data
}

# Save to JSON file
with open('city_data.json', 'w') as f:
    json.dump(unified_record, f, indent=2)

print("Data saved to city_data.json")

# Generate report
report = f"""
City Data Report for {city}
==========================

Timestamp: {unified_record['timestamp']}

Weather Information:
{json.dumps(unified_record['weather'], indent=2) if unified_record['weather'] else 'Not available'}

Geolocation Information:
{json.dumps(unified_record['geolocation'], indent=2) if unified_record['geolocation'] else 'Not available'}

Timezone Information:
{json.dumps(unified_record['timezone'], indent=2) if unified_record['timezone'] else 'Not available'}
"""

print(report)

# Print the most complete record
print("\nMost Complete Record:")
print(json.dumps(unified_record, indent=2))