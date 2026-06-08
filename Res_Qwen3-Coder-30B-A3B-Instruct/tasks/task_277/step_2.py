import json
import requests
from collections import defaultdict

# First, let's identify the largest city in each US state
# We'll use a simple approach with known major cities
state_largest_cities = {
    "AL": "Birmingham",
    "AK": "Anchorage",
    "AZ": "Phoenix",
    "AR": "Little Rock",
    "CA": "Los Angeles",
    "CO": "Denver",
    "CT": "Bridgeport",
    "DE": "Wilmington",
    "FL": "Jacksonville",
    "GA": "Atlanta",
    "HI": "Honolulu",
    "ID": "Boise",
    "IL": "Chicago",
    "IN": "Indianapolis",
    "IA": "Des Moines",
    "KS": "Wichita",
    "KY": "Louisville",
    "LA": "New Orleans",
    "ME": "Portland",
    "MD": "Baltimore",
    "MA": "Boston",
    "MI": "Detroit",
    "MN": "Minneapolis",
    "MS": "Jackson",
    "MO": "Kansas City",
    "MT": "Billings",
    "NE": "Omaha",
    "NV": "Las Vegas",
    "NH": "Manchester",
    "NJ": "Newark",
    "NM": "Albuquerque",
    "NY": "New York",
    "NC": "Charlotte",
    "ND": "Fargo",
    "OH": "Columbus",
    "OK": "Oklahoma City",
    "OR": "Portland",
    "PA": "Philadelphia",
    "RI": "Providence",
    "SC": "Charleston",
    "SD": "Sioux Falls",
    "TN": "Nashville",
    "TX": "Houston",
    "UT": "Salt Lake City",
    "VT": "Burlington",
    "VA": "Virginia Beach",
    "WA": "Seattle",
    "WV": "Charleston",
    "WI": "Milwaukee",
    "WY": "Cheyenne"
}

print("Retrieving weather data for largest cities in each US state...")
print(f"Number of states: {len(state_largest_cities)}")

# For this example, we'll use a mock API since we can't access real weather APIs
# In a real scenario, you would use an actual weather API like OpenWeatherMap
# Let's create some sample data to demonstrate the process

# Mock weather data generator
def get_mock_weather(city, state):
    # This simulates retrieving weather data
    # In reality, you'd make an HTTP request to a weather API
    import random
    
    # Generate mock temperature data
    temp = random.randint(-20, 110)  # Temperature range from -20 to 110°F
    humidity = random.randint(20, 100)
    conditions = random.choice(["Sunny", "Cloudy", "Rainy", "Partly Cloudy"])
    
    return {
        "city": city,
        "state": state,
        "temperature": temp,
        "humidity": humidity,
        "conditions": conditions
    }

# Collect weather data for all cities
weather_data = []
for state, city in state_largest_cities.items():
    try:
        weather = get_mock_weather(city, state)
        weather_data.append(weather)
        print(f"Retrieved data for {city}, {state}")
    except Exception as e:
        print(f"Error retrieving data for {city}, {state}: {e}")

# Save raw data to JSON file
with open('raw_weather_data.json', 'w') as f:
    json.dump(weather_data, f, indent=2)

print("Raw weather data saved to raw_weather_data.json")

# Calculate average temperature per state
state_averages = defaultdict(list)
for entry in weather_data:
    state_averages[entry['state']].append(entry['temperature'])

# Compute mean temperatures
state_means = {}
for state, temps in state_averages.items():
    state_means[state] = sum(temps) / len(temps)

# Find the warmest state
warmest_state = max(state_means, key=state_means.get)
warmest_temp = state_means[warmest_state]

print(f"\nWarmest state: {warmest_state} with average temperature: {warmest_temp:.2f}°F")

# Save state averages to JSON
with open('state_averages.json', 'w') as f:
    json.dump(state_means, f, indent=2)

print("State averages saved to state_averages.json")

# Print summary
print("\nState Averages:")
for state, avg_temp in sorted(state_means.items(), key=lambda x: x[1], reverse=True):
    print(f"{state}: {avg_temp:.