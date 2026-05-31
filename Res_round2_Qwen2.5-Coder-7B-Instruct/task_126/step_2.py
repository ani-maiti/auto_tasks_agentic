import socket

# Check if the domain name can be resolved
def check_domain_resolution(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

domain = "www.boredapi.com"
if check_domain_resolution(domain):
    print(f"Domain {domain} is resolvable.")
else:
    print(f"Domain {domain} is not resolvable. Please check your network connection.")