import json
from collections import defaultdict

# Now let's cluster cities by temperature ranges
# Define temperature ranges
temp_ranges = [
    (-50, 0),    # Very cold
    (0, 10),     # Cold
    (10, 20),    # Cool
    (20, 30),    # Warm
    (30, 50)     # Hot
]

# Create clusters
clusters = defaultdict(list)

for city_data in weather_data:
    temp = city_data["main"]["temp"]
    city_name = city_data["name"]
    
    # Find appropriate temperature range
    assigned = False
    for i, (min_temp, max_temp) in enumerate(temp_ranges):
        if min_temp <= temp < max_temp:
            clusters[f"{min_temp}-{max_temp}°C"].append(city_name)
            assigned = True
            break
    
    # Handle edge cases
    if not assigned:
        if temp >= 50:
            clusters["50°C+"].append(city_name)
        elif temp < 0:
            clusters["Below 0°C"].append(city_name)

# Print all clusters
print("Temperature Clusters:")
for temp_range, cities_in_cluster in clusters.items():
    print(f"{temp_range}: {len(cities_in_cluster)} cities")
    print(f"  Cities: {', '.join(cities_in_cluster)}")
    print()

# Find the largest cluster
largest_cluster = max(clusters.items(), key=lambda x: len(x[1]))
print(f"Largest cluster: {largest_cluster[0]} with {len(largest_cluster[1])} cities")

# Save clustered results
clustered_data = {
    "clusters": dict(clusters),
    "largest_cluster": {
        "range": largest_cluster[0],
        "count": len(largest_cluster[1]),
        "cities": largest_cluster[1]
    }
}

with open('clustered_weather_data.json', 'w') as f:
    json.dump(clustered_data, f, indent=2)

print("\nClustered data saved to clustered_weather_data.json")