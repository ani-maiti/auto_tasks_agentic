import json
from operator import itemgetter

# Load the disconnected documentation groups from JSON
with open('disconnected_groups.json', 'r') as f:
    disconnected_groups = json.load(f)

# Check if there are any disconnected groups
if disconnected_groups:
    # Sort the groups by size
    sorted_groups = sorted(disconnected_groups, key=len, reverse=True)

    # Print the largest connected component
    largest_group = sorted_groups[0]
    print("Largest connected component:")
    for group in largest_group:
        print(group)
else:
    print("No disconnected documentation groups found.")