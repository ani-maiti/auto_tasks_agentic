import socket

# Step 2: Check if the domain name can be resolved
domain = "example.gov"
try:
    ip_address = socket.gethostbyname(domain)
    print(f"Domain {domain} resolves to IP address {ip_address}")
except socket.gaierror:
    print(f"Domain {domain} could not be resolved")
    exit(1)