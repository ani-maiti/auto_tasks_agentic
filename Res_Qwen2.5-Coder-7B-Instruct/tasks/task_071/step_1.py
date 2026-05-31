import datetime
from astral.sun import sun
from astral import LocationInfo

# Define location
location = LocationInfo("London", "UK")

# Get current date
now = datetime.datetime.now()

# Calculate sunrise and sunset
s = sun(location.observer, date=now)

print(f"Sunrise in London today: {s['sunrise']}")
print(f"Sunset in London today: {s['sunset']}")