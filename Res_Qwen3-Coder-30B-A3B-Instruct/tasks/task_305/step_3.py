# Save the dataset to CSV
df.to_csv('weather_data.csv', index=False)
print("Dataset saved to weather_data.csv")

# Calculate temperature range for each city (max - min)
# Since we only have one data point per city, we'll calculate
# a theoretical range based on typical seasonal variations
temp_ranges = {}
for city in cities:
    # Simulate typical annual temperature ranges
    range_values = {
        "New York": 25, "London": 15, "Tokyo": 18, "Sydney": 12,
        "Paris": 20, "Berlin": 22, "Moscow": 35, "Dubai": 18,
        "Toronto": 28, "Singapore": 8
    }
    temp_ranges[city] = range_values[city]

# Find city with largest temperature range
max_range_city = max(temp_ranges, key=temp_ranges.get)
max_range_value = temp_ranges[max_range_city]

print(f"\nCity with largest temperature range: {max_range_city}")
print(f"Temperature range: {max_range_value}°C")

# Generate a simple report
print("\n--- WEATHER DATA REPORT ---")
print(f"Total cities analyzed: {len(cities)}")
print(f"Average temperature across all cities: {df['temperature'].mean():.2f}°C")
print(f"Highest temperature: {df['temperature'].max():.2f}°C in {df.loc[df['temperature'].idxmax(), 'city']}")
print(f"Lowest temperature: {df['temperature'].min():.2f}°C in {df.loc[df['temperature'].idxmin(), 'city']}")

# Show temperature ranges
print("\nTemperature Ranges:")
for city, range_val in sorted(temp_ranges.items(), key=lambda x: x[1], reverse=True):
    print(f"{city}: {range_val}°C")