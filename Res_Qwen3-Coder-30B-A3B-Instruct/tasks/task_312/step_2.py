import requests
import json
from datetime import datetime

# Since we don't have valid API keys, let's use mock data to demonstrate the process
# In a real scenario, you would need to sign up for free API keys at:
# - OpenWeatherMap: https://openweathermap.org/api
# - Or use alternative free APIs

# Mock data for demonstration purposes
mock_weather_data = {
    "name": "London",
    "main": {
        "temp": 280.32,
        "feels_like": 278.05,
        "temp_min": 279.15,
        "temp_max": 281.15,
        "pressure": 1012,
        "humidity": 81
    },
    "weather": [
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01d"
        }
    ],
    "wind": {
        "speed": 3.6,
        "deg": 300
    }
}

mock_geo_data = {
    "name": "London",
    "lat": 51.5074,
    "lon": -0.1278,
    "country": "GB",
    "state": "England"
}

mock_timezone_data = {
    "abbreviation": "BST",
    "client_ip": "192.168.1.1",
    "datetime": "2026-06-02T06:03:31.295394+01:00",
    "day_of_week": 2,
    "day_of_year": 153,
    "dst": True,
    "dst_from": "2026-03-29T01:00:00+00:00",
    "dst_offset": 3600,
    "dst_until": "2026-10-25T01:00:00+00:00",
    "raw_offset": 3600,
    "timezone": "Europe/London",
    "unixtime": 1780423411,
    "utc_datetime": "2026-06-02T05:03:31.295394+00:00",
    "utc_offset": "+01:00",
    "week_number": 22
}

# Create unified record with mock data
unified_record = {
    "city": "London",
    "timestamp": datetime.now().isoformat(),
    "weather": mock_weather_data,
    "geolocation": mock_geo_data,
    "timezone": mock_timezone_data
}

# Save to JSON file
with open('city_data.json', 'w') as f:
    json.dump(unified_record, f, indent=2)

print("Mock data saved to city_data.json")

# Generate report
report = f"""
City Data Report for London
==========================

Timestamp: {unified_record['timestamp']}

Weather Information:
Temperature: {unified_record['weather']['main']['temp']}K
Feels like: {unified_record['weather']['main']['feels_like']}K
Description: {unified_record['weather']['weather'][0]['description']}
Wind Speed: {unified_record['weather']['wind']['speed']}m/s

Geolocation Information:
Latitude: {unified_record['geolocation']['lat']}
Longitude: {unified_record['geolocation']['lon']}
Country: {unified_record['geolocation']['country']}
State: {unified_record['geolocation']['state']}

Timezone Information:
Timezone: {unified_record['timezone']['timezone']}
UTC Offset: {unified_record['timezone']['utc_offset']}
DST: {'Yes' if unified_record['timezone']['dst'] else 'No'}
"""

print(report)

# Print the most complete record
print("\nMost Complete Record:")
print(json.dumps(unified_record, indent=2))