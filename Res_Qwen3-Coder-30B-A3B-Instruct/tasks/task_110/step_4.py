import socket

def get_nameservers(domain):
    try:
        # Get the authoritative nameservers for the domain
        ns_records = socket.getaddrinfo(domain, None, socket.AF_INET, socket.SOCK_STREAM)
        return [record[4][0] for record in ns_records]
    except Exception as e:
        return str(e)

# Try to get nameservers for python.org
nameservers = get_nameservers("python.org")
print(nameservers)