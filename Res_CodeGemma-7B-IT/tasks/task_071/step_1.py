from datetime import datetime
import pytz

# Set the time zone for London
london_tz = pytz.timezone('Europe/London')

# Get the current date and time in London
current_datetime = datetime.now(london_tz)

# Get the sunrise and sunset times for today in London
sunrise_time = london_tz.localize(datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0))
sunset_time = london_tz.localize(datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=0))

# Print the sunrise and sunset times
print("Today's sunrise time in London is:", sunrise_time)
print("Today's sunset time in London is:", sunset_time)