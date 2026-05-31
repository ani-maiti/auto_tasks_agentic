import json

# Save to JSON
with open('combined_schema.json', 'w') as f:
    json.dump(combined_schema, f, indent=4)

print("Combined schema saved to combined_schema.json")