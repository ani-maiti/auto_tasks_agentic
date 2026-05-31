import os
import re

# List all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Regular expression pattern for matching IPv4 addresses
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Initialize an empty list to store extracted IP addresses
ip_addresses = []

# Loop through each file and extract IPv4 addresses
for file in files:
    with open(file, 'r') as f:
        content = f.read()
        matches = re.findall(ipv4_pattern, content)
        ip_addresses.extend(matches)

# Print the extracted IP addresses
print(ip_addresses)