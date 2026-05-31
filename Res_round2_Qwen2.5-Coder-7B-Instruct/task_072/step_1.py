import datetime
from astral.sun import sun
from astral import LocationInfo

# Define location
location = LocationInfo("New York", "US/Eastern")

# Get current date
now = datetime.datetime.now()

# Calculate sunrise and sunset
s = sun(location.observer, date=now)

# Print results
print(f"Sunrise in New York today: {s['sunrise']}")
print(f"Sunset in New York today: {s['sunset']}")