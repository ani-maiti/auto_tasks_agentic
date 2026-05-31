import re

# Function to extract IPv4 addresses from a text file
def extract_ipv4_addresses(file_path):
    with open(file_path, "r") as f:
        text = f.read()
        ipv4_addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", text)
    return ipv4_addresses

# Function to group addresses by subnet
def group_by_subnet(ipv4_addresses):
    subnets = {}
    for address in ipv4_addresses:
        subnet = ".".join(address.split(".")[:2]) + ".0/24"
        if subnet not in subnets:
            subnets[subnet] = []
        subnets[subnet].append(address)
    return subnets

# Function to generate a frequency report
def generate_frequency_report(subnets):
    subnet_frequencies = {subnet: len(addresses) for subnet, addresses in subnets.items()}
    sorted_subnets = sorted(subnet_frequencies.items(), key=lambda item: item[1], reverse=True)
    return sorted_subnets

# Get the file path from the user
file_path = input("Enter the file path: ")

# Extract IPv4 addresses from the text file
ipv4_addresses = extract_ipv4_addresses(file_path)

# Group addresses by subnet
subnets = group_by_subnet(ipv4_addresses)

# Generate a frequency report
frequency_report = generate_frequency_report(subnets)

# Print the most common subnet
print("Most common subnet:", frequency_report[0][0])