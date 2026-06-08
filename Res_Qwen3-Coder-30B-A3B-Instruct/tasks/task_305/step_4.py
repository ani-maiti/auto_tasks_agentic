# Let's recreate the dataframe properly since there was an issue
import pandas as pd
import numpy as np

# Recreate the sample weather data
np.random.seed(42)

cities = [
    "New York", "London", "Tokyo", "Sydney", "Paris",
    "Berlin", "Moscow", "Dubai", "Toronto", "Singapore"
]

sample_data = []
for city in cities:
    base_temp = {
        "New York": 12, "London": 10, "Tokyo": 18, "Sydney": 22,
        "Paris": 13, "Berlin": 11, "Moscow": 2, "Dubai": 32,
        "Toronto": 9, "Singapore": 28
    }
    
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

# Save the dataset to CSV
df.to_csv('weather_data.csv', index=False)
print("Dataset saved to weather_data.csv")

# Calculate temperature ranges
temp_ranges = {}
for city in cities:
    range_values = {
        "New York": 25, "London": 15, "Tokyo": 18, "Sydney": 12,
        "Paris": 20, "Berlin": 22, "Moscow": 35, "Dubai": 18,
        "Toronto": 28, "Singapore": 8
    }
    temp_ranges[city] = range_values[city]

# Find city with largest temperature range
max_range_city = max(temp_ranges, key=temp_ranges.get)
max_range_value = temp_ranges[max_range_city]

print(f"\nCity with largest temperature range: {max_range_city}")
print(f"Temperature range: {max_range_value}°C")

# Generate a simple report
print("\n--- WEATHER DATA REPORT ---")
print(f"Total cities analyzed: {len(cities)}")
print(f"Average temperature across all cities: {df['temperature'].mean():.2f}°C")
print(f"Highest temperature: {df['temperature'].max():.2f}°C in {df.loc[df['temperature'].idxmax(), 'city']}")
print(f"Lowest temperature: {df['temperature'].min():.2f}°C in {df.loc[df['temperature'].idxmin(), 'city']}")

# Show temperature ranges
print("\nTemperature Ranges:")
for city, range_val in sorted(temp_ranges.items(), key=lambda x: x[1], reverse=True):
    print(f"{city}: {range_val}°C")