from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# Get list of largest US cities
cities_url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"
cities_html = urlopen(cities_url).read().decode('utf-8')
cities_soup = BeautifulSoup(cities_html, 'html.parser')

cities = []
for row in cities_soup.find_all('tr')[1:]:
    city_name = row.find_all('td')[1].text.strip()
    state = row.find_all('td')[3].text.strip()
    cities.append((city_name, state))

# Get weather data for each city
weather_data = []
for city_name, state in cities:
    weather_url = f"https://www.accuweather.com/en/us/{city_name}/27201/weather-forecast/329448"
    weather_html = urlopen(weather_url).read().decode('utf-8')
    weather_soup = BeautifulSoup(weather_html, 'html.parser')

    temperature = weather_soup.find('span', class_="wu-value wu-value-to").text.strip()
    weather_data.append({
        'city': city_name,
        'state': state,
        'temperature': temperature
    })

# Compute state averages
state_averages = {}
for data in weather_data:
    state = data['state']
    temperature = float(data['temperature'][:-1])
    if state not in state_averages:
        state_averages[state] = []
    state_averages[state].append(temperature)

for state, temperatures in state_averages.items():
    state_averages[state] = sum(temperatures) / len(temperatures)

# Save results to JSON
with open('weather_data.json', 'w') as f:
    json.dump(state_averages, f)

# Print warmest state
warmest_state = max(state_averages, key=state_averages.get)
print(f"The warmest state is {warmest_state} with an average temperature of {state_averages[warmest_state]}.")