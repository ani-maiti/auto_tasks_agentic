import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time

# Since we can't use the OpenWeatherMap API due to authentication issues,
# let's create a mock dataset instead to demonstrate the workflow

# Mock data for 50 major cities
mock_cities = [
    "New York", "London", "Tokyo", "Paris", "Sydney", "Dubai", "Singapore", "Toronto",
    "Berlin", "Rome", "Madrid", "Amsterdam", "Stockholm", "Copenhagen", "Oslo", "Helsinki",
    "Athens", "Istanbul", "Moscow", "Bangkok", "Seoul", "Shanghai", "Beijing", "Mumbai",
    "Karachi", "Lagos", "Cairo", "Johannesburg", "São Paulo", "Mexico City", "Buenos Aires",
    "Rio de Janeiro", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
    "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", 
    "Charlotte", "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington", "Boston"
]

# Create mock weather data
np.random.seed(42)  # For reproducible results
mock_data = []

for city in mock_cities:
    # Generate 40 forecast entries (5 days * 8 per day)
    for i in range(40):
        timestamp = datetime.now() + timedelta(hours=i*3)
        # Simulate temperature variations with some randomness
        base_temp = np.random.normal(20, 10)  # Mean 20°C, std dev 10°C
        temp = base_temp + np.random.normal(0, 5)  # Add some noise
        humidity = np.random.randint(30, 90)
        pressure = np.random.randint(1000, 1030)
        wind_speed = np.random.uniform(0, 20)
        
        mock_data.append({
            'city': city,
            'timestamp': timestamp,
            'temperature': round(temp, 2),
            'humidity': humidity,
            'pressure': pressure,
            'wind_speed': round(wind_speed, 2)
        })

# Convert to DataFrame
df = pd.DataFrame(mock_data)
print(f"Created mock dataset with {len(df)} entries")

# Save raw data
df.to_csv('weather_data_raw.csv', index=False)
print("Raw data saved to weather_data_raw.csv")

def calculate_volatility(df):
    """Calculate volatility as standard deviation of temperatures"""
    volatility = df.groupby('city')['temperature'].std().reset_index()
    volatility.columns = ['city', 'volatility']
    return volatility

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