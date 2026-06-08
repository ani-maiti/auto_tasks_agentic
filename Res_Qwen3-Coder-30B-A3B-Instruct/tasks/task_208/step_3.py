import json

# Check the structure of one of the response files to understand the data format
with open("New York_weather.json", "r") as f:
    data = json.load(f)
    print("Sample data structure:")
    print(json.dumps(data, indent=2))