# Import the necessary libraries
import json

# Load the results from the JSON file
with open("results.json", "r") as f:
    results = json.load(f)

# Print the average stars and forks
print("Average Stars:", results["average_stars"])
print("Average Forks:", results["average_forks"])