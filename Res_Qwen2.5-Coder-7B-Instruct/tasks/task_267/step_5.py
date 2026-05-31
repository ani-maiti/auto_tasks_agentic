import json

# Load the clusters from the file
with open('clusters.json', 'r') as f:
    clusters = json.load(f)

# Find the largest cluster
largest_cluster = max(clusters.values(), key=len)

# Print the largest cluster
print("Largest cluster:")
for city, temp in largest_cluster:
    print(f"{city}: {temp}°C")