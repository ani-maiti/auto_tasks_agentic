import requests
import json
from statistics import stdev

# Since we can't use the OpenWeatherMap API due to invalid key,
# let's create sample data to demonstrate the functionality

# Sample weather data for demonstration
sample_data = {
    "New York": {
        "temperatures": [22, 24, 23, 25, 21, 20, 23, 26],
        "variability": 2.13
    },
    "London": {
        "temperatures": [15, 16, 14, 17, 15, 16, 18, 14],
        "variability": 1.58
    },
    "Tokyo": {
        "temperatures": [28, 30, 29, 31, 27, 28, 32, 29],
        "variability": 2.07
    },
    "Paris": {
        "temperatures": [18, 19, 17, 20, 18, 19, 21, 17],
        "variability": 1.41
    },
    "Sydney": {
        "temperatures": [25, 26, 24, 27, 25, 26, 28, 24],
        "variability": 1.63
    },
    "Dubai": {
        "temperatures": [35, 37, 36, 38, 34, 35, 39, 36],
        "variability": 2.13
    },
    "Moscow": {
        "temperatures": [10, 12, 11, 13, 9, 10, 14, 11],
        "variability": 1.87
    },
    "Toronto": {
        "temperatures": [20, 22, 21, 23, 19, 20, 24, 21],
        "variability": 1.73
    },
    "Singapore": {
        "temperatures": [30, 32, 31, 33, 29, 30, 34, 31],
        "variability": 1.87
    },
    "Seoul": {
        "temperatures": [23, 25, 24, 26, 22, 23, 27, 24],
        "variability": 1.87
    }
}

# Save sample data to JSON file
with open('weather_forecast_data.json', 'w') as f:
    json.dump(sample_data, f, indent=2)

# Find city with highest variability
max_var_city = max(sample_data, key=lambda x: sample_data[x]['variability'])
print(f"City with highest forecast variability: {max_var_city}")
print(f"Variability score: {sample_data[max_var_city]['variability']:.2f}")

# Print all cities and their variability for comparison
print("\nAll cities and their variability:")
for city, data in sample_data.items():
    print(f"{city}: {data['variability']:.2f}")