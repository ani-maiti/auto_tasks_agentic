import json

# Load the weather data from the file
with open('weather_data.json', 'r') as f:
    weather_data = json.load(f)

# Extract temperatures
temperatures = [data for data in weather_data.values()]

# Sort temperatures
sorted_temperatures = sorted(temperatures)

# Define temperature ranges
ranges = [
    (-float('inf'), 10),
    (10, 20),
    (20, 30),
    (30, 40),
    (40, float('inf'))
]

# Initialize clusters
clusters = {f"Range {i+1}": [] for i in range(len(ranges))}

# Assign cities to clusters
for city, temp in weather_data.items():
    for i, (low, high) in enumerate(ranges):
        if low < temp <= high:
            clusters[f"Range {i+1}"].append((city, temp))
            break

# Save the clusters to a file
with open('clusters.json', 'w') as f:
    json.dump(clusters, f)

print("Clusters saved.")