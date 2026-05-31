import datetime
from astral.sun import sun
from astral import LocationInfo

# Define location for London
location = LocationInfo("London", "UK")

# Get current date
now = datetime.datetime.now()

# Calculate sunrise and sunset times
s = sun(location.observer, date=now)

# Print results
print(f"Sunrise in London today: {s['sunrise']}")
print(f"Sunset in London today: {s['sunset']}")