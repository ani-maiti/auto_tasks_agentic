import requests

# Try a different random activity API
response = requests.get("https://api.random.org/json-rpc/2/invoke", timeout=10)

# If that doesn't work, try a simple curl command to test connectivity
print("Testing network connectivity...")