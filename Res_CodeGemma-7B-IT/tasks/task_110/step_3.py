# The nameservers were not printed in the previous step, so we need to re-execute the first code block to get the socket object
import socket

# Set the domain name
domain_name = "python.org"

# Create a socket object
socket_obj = socket.gethostbyname(domain_name)

# Print the nameservers
print(socket_obj)
```
execution trace:
stdout:
151.101.0.223


stderr:


return code: 0