import socket

try:
    # Get A records for github.com
    records = socket.getaddrinfo('github.com', None, socket.AF_INET)
    
    # Extract just the IP addresses
    ip_addresses = set()
    for record in records:
        ip_addresses.add(record[4][0])
    
    # Print the results
    for ip in sorted(ip_addresses):
        print(ip)
        
except Exception as e:
    print(f"Error: {e}")