# Convert times to local time without timezone info
sunrise_local = s['sunrise'].replace(tzinfo=None)
sunset_local = s['sunset'].replace(tzinfo=None)

# Print local times
print(f"Sunrise in New York today (local time): {sunrise_local}")
print(f"Sunset in New York today (local time): {sunset_local}")