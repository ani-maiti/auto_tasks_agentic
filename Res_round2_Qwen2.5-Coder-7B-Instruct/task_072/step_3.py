# Ensure the necessary imports are included
import datetime
from astral.sun import sun
from astral import LocationInfo

# Define location
location = LocationInfo("New York", "US/Eastern")

# Get current date
now = datetime.datetime.now()

# Calculate sunrise and sunset
s = sun(location.observer, date=now)

# Convert times to local timezone
local_sunrise = s['sunrise'].astimezone(location.tzinfo)
local_sunset = s['sunset'].astimezone(location.tzinfo)

# Print local times
print(f"Local Sunrise in New York today: {local_sunrise}")
print(f"Local Sunset in New York today: {local_sunset}")