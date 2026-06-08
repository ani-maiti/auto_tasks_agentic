import requests
import pandas as pd
import numpy as np
from collections import defaultdict
import json

# First, let's get the list of largest cities by state
# We'll use a simple approach - just get the capital city for each state
# since capitals are often the largest cities
states_info = {
    'AL': 'Montgomery', 'AK': 'Juneau', 'AZ': 'Phoenix', 'AR': 'Little Rock',
    'CA': 'Sacramento', 'CO': 'Denver', 'CT': 'Hartford', 'DE': 'Dover',
    'FL': 'Tallahassee', 'GA': 'Atlanta', 'HI': 'Honolulu', 'ID': 'Boise',
    'IL': 'Springfield', 'IN': 'Indianapolis', 'IA': 'Des Moines', 'KS': 'Topeka',
    'KY': 'Frankfort', 'LA': 'Baton Rouge', 'ME': 'Augusta', 'MD': 'Annapolis',
    'MA': 'Boston', 'MI': 'Lansing', 'MN': 'Saint Paul', 'MS': 'Jackson',
    'MO': 'Jefferson City', 'MT': 'Helena', 'NE': 'Lincoln', 'NV': 'Carson City',
    'NH': 'Concord', 'NJ': 'Trenton', 'NM': 'Santa Fe', 'NY': 'Albany',
    'NC': 'Raleigh', 'ND': 'Bismarck', 'OH': 'Columbus', 'OK': 'Oklahoma City',
    'OR': 'Salem', 'PA': 'Harrisburg', 'RI': 'Providence', 'SC': 'Columbia',
    'SD': 'Pierre', 'TN': 'Nashville', 'TX': 'Austin', 'UT': 'Salt Lake City',
    'VT': 'Montpelier', 'VA': 'Richmond', 'WA': 'Olympia', 'WV': 'Charleston',
    'WI': 'Madison', 'WY': 'Cheyenne'
}

print("Retrieving weather data for largest cities in each US state...")
print(f"Number of cities to query: {len(states_info)}")

# Get API key from environment or use a placeholder
try:
    api_key = open('weather_api_key.txt').read().strip()
except FileNotFoundError:
    # For this example, we'll use a placeholder
    api_key = "YOUR_API_KEY_HERE"

# Store all weather data
all_weather_data = []

# Query weather data for each city
for state_code, city in states_info.items():
    try:
        # Using OpenWeatherMap API (free tier available)
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': f"{city},US-{state_code}",
            'appid': api_key,
            'units': 'metric'  # Use Celsius
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather_entry = {
                'state': state_code,
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'description': data['weather'][0]['description'],
                'wind_speed': data['wind']['speed']
            }
            all_weather_data.append(weather_entry)
            print(f"✓ Retrieved data for {city}, {state_code}")
        else:
            print(f"✗ Failed to retrieve data for {city}, {state_code}: {response.status_code}")
    except Exception as e:
        print(f"✗ Error retrieving data for {city}, {state_code}: {str(e)}")

print(f"\nSuccessfully retrieved data for {len(all_weather_data)} cities")