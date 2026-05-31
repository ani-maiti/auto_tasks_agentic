# Import the json module
import json

# Save the JSON summary to a file
with open('file_sizes.json', 'w') as f:
    json.dump(json_summary, f, indent=4)

# Print confirmation message
print("JSON summary saved to file_sizes.json")