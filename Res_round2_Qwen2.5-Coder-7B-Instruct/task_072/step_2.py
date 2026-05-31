# Convert times to local timezone
local_sunrise = s['sunrise'].astimezone(location.tzinfo)
local_sunset = s['sunset'].astimezone(location.tzinfo)

# Print local times
print(f"Local Sunrise in New York today: {local_sunrise}")
print(f"Local Sunset in New York today: {local_sunset}")