# Define function to scrape weather data for a city
def get_weather_data(city):
    url = f"https://www.weather.gov/climate/monthly-averages?city={city}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # ... (Scrape data from the webpage)
    return weather_data