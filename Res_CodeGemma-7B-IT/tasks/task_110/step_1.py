import socket

# Set the domain name
domain_name = "python.org"

# Create a socket object
socket_obj = socket.gethostbyname(domain_name)

# Print the nameservers
print(socket_obj)