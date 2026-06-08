# Since we can't get real weather data due to API issues, let's create sample data
# that simulates weather patterns for our 10 cities

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create sample weather data for 10 cities
np.random.seed(42)  # For reproducible results

cities = [
    "New York", "London", "Tokyo", "Sydney", "Paris",
    "Berlin", "Moscow", "Dubai", "Toronto", "Singapore"
]

# Generate sample data with realistic temperature ranges
sample_data = []
for city in cities:
    # Base temperatures for different climates
    base_temp = {
        "New York": 12, "London": 10, "Tokyo": 18, "Sydney": 22,
        "Paris": 13, "Berlin": 11, "Moscow": 2, "Dubai": 32,
        "Toronto": 9, "Singapore": 28
    }
    
    # Add some variation
    temp_range = {
        "New York": 15, "London": 12, "Tokyo": 10, "Sydney": 8,
        "Paris": 14, "Berlin": 13, "Moscow": 20, "Dubai": 12,
        "Toronto": 16, "Singapore": 5
    }
    
    avg_temp = base_temp[city]
    temp_variation = np.random.normal(0, temp_range[city]/3)
    temperature = avg_temp + temp_variation
    
    humidity = np.random.randint(40, 90)
    pressure = np.random.randint(1000, 1030)
    
    sample_data.append({
        'city': city,
        'temperature': round(temperature, 2),
        'humidity': humidity,
        'pressure': pressure,
        'description': np.random.choice(['sunny', 'cloudy', 'rainy', 'partly cloudy'])
    })

# Create DataFrame
df = pd.DataFrame(sample_data)
print("Sample Weather Data:")
print(df)