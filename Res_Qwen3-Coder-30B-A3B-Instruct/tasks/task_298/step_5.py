# Let's create a simpler mock dataset without complex nested structures
import pandas as pd
import numpy as np

# Create mock weather data for demonstration purposes
np.random.seed(42)  # For reproducible results

# State abbreviations and their largest cities (capitals)
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

# Generate mock data
mock_data = []
for state_code, city in states_info.items():
    # Simple temperature range based on general climate
    base_temp = 20  # Base temperature
    
    # Adjust based on approximate latitude and climate
    if state_code in ['HI', 'FL', 'GA', 'NC', 'SC']:
        base_temp = 25  # Southern states
    elif state_code in ['CA', 'OR', 'WA']:
        base_temp = 18  # Pacific coast
    elif state_code in ['TX', 'OK', 'KS', 'NE']:
        base_temp = 22  # Central plains
    elif state_code in ['MN', 'WI', 'IL', 'IN', 'OH']:
        base_temp = 15  # Midwest
    elif state_code in ['MT', 'ND', 'SD', 'WY', 'ID']:
        base_temp = 10  # Northern plains
    elif state_code in ['AK']:
        base_temp = 5   # Alaska
    elif state_code in ['CO', 'UT', 'NM']:
        base_temp = 18  # Mountain states
    
    # Add some random variation
    temperature = round(np.random.normal(base_temp, 5), 1)
    
    # Generate other weather parameters
    humidity = round(np.random.uniform(40, 90), 1)
    pressure = round(np.random.uniform(1000, 1030), 1)
    wind_speed = round(np.random.uniform(0, 15), 1)
    
    weather_entry = {
        'state': state_code,
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure,
        'description': 'Partly cloudy',
        'wind_speed': wind_speed
    }
    mock_data.append(weather_entry)

# Create DataFrame
df = pd.DataFrame(mock_data)
print("Mock weather data created successfully")
print(df.head())