import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# List of 50 major cities worldwide
cities = [
    "New York", "London", "Tokyo", "Paris", "Sydney", "Dubai", "Singapore", "Toronto",
    "Berlin", "Rome", "Madrid", "Amsterdam", "Stockholm", "Copenhagen", "Oslo", "Helsinki",
    "Athens", "Istanbul", "Moscow", "Bangkok", "Seoul", "Shanghai", "Beijing", "Mumbai",
    "Karachi", "Lagos", "Cairo", "Johannesburg", "São Paulo", "Mexico City", "Buenos Aires",
    "Rio de Janeiro", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
    "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", 
    "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston"
]

# OpenWeatherMap API key (using a placeholder - in reality this would be a real key)
API_KEY = "YOUR_API_KEY_HERE"

def get_weather_data(city):
    """Fetch weather data for a given city"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for {city}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception for {city}: {str(e)}")
        return None

def normalize_weather_data(data):
    """Normalize weather data into a common format"""
    if not data:
        return None
    
    normalized = []
    city_name = data['city']['name']
    
    # Process forecast data for next 7 days
    for item in data['list'][:40]:  # Take first 5 days (8*5 = 40 entries)
        timestamp = datetime.fromtimestamp(item['dt'])
        temp = item['main']['temp']
        humidity = item['main']['humidity']
        pressure = item['main']['pressure']
        wind_speed = item['wind']['speed']
        
        normalized.append({
            'city': city_name,
            'timestamp': timestamp,
            'temperature': temp,
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': wind_speed
        })
    
    return normalized

def calculate_volatility(df):
    """Calculate volatility as standard deviation of temperatures"""
    volatility = df.groupby('city')['temperature'].std().reset_index()
    volatility.columns = ['city', 'volatility']
    return volatility

# Main execution
all_data = []

print("Fetching weather data for cities...")
for i, city in enumerate(cities):
    print(f"Processing {city} ({i+1}/{len(cities)})")
    raw_data = get_weather_data(city)
    normalized_data = normalize_weather_data(raw_data)
    
    if normalized_data:
        all_data.extend(normalized_data)
    
    # Be respectful to API limits
    time.sleep(1)

print(f"Retrieved data for {len(all_data)} entries")

# Convert to DataFrame
df = pd.DataFrame(all_data)
print(f"DataFrame shape: {df.shape}")

# Save raw data
df.to_csv('weather_data_raw.csv', index=False)
print("Raw data saved to weather_data_raw.csv")

# Calculate volatility
volatility_df = calculate_volatility(df)
print("Volatility calculated")

# Rank cities by volatility
volatility_df = volatility_df.sort_values('volatility', ascending=False)
print("Cities ranked by volatility")

# Save volatility data
volatility_df.to_csv('weather_volatility.csv', index=False)
print("Volatility data saved to weather_volatility.csv")

# Generate summary report
summary_report = {
    'total_cities': len(volatility_df),
    'most_volatile_city': volatility_df.iloc[0]['city'],
    'highest_volatility': volatility_df.iloc[0]['volatility'],
    'average_volatility': volatility_df['volatility'].mean(),
    'median_volatility': volatility_df['volatility'].median()
}

print("Summary Report:")
for key, value in summary_report.items():
    print(f"{key}: {value}")

# Print the most volatile city
print(f"\nMost volatile city: {volatility_df.iloc[0]['city']} with volatility: {volatility_df.iloc[0]['volatility']:.2f}")