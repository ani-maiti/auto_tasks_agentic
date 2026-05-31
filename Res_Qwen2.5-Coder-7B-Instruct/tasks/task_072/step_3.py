# Ensure the correct variable is used
sunrise_local = s['sunrise'].astimezone(timezone('America/New_York')).replace(tzinfo=None)
sunset_local = s['sunset'].astimezone(timezone('America/New_York')).replace(tzinfo=None)

# Print local times
print(f"Sunrise in New York today (local time): {sunrise_local}")
print(f"Sunset in New York today (local time): {sunset_local}")