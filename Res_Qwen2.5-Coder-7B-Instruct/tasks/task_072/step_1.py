import datetime
from pytz import timezone
from astral.sun import sun
from astral import LocationInfo

# Define location
location = LocationInfo("New York", "USA")

# Get current date and time
now = datetime.datetime.now(timezone('America/New_York'))

# Calculate sunrise and sunset times
s = sun(location.observer, date=now)

# Print results
print(f"Sunrise in New York today: {s['sunrise']}")
print(f"Sunset in New York today: {s['sunset']}")