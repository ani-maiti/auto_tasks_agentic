import socket

# Check if DNS resolution works for api.coindesk.com
try:
    socket.gethostbyname('api.coindesk.com')
    print("DNS resolution successful.")
except socket.gaierror as e:
    print(f"DNS resolution failed: {e}")

# If DNS resolution fails, try fetching the IP address manually
if 'gaierror' in str(e):
    import dns.resolver
    try:
        answers = dns.resolver.resolve('api.coindesk.com', 'A')
        ip_address = answers[0].address
        print(f"Resolved IP address: {ip_address}")
    except dns.resolver.NoAnswer:
        print("No answer found for DNS query.")
    except dns.resolver.NXDOMAIN:
        print("Domain name does not exist.")
    except Exception as e:
        print(f"An error occurred while resolving DNS: {e}")
```

This code attempts to resolve the domain name `api.coindesk.com` using both the standard Python socket library and the `dnspython` library. If the domain name can be resolved, it prints the IP address. If not, it handles the exceptions and provides appropriate feedback.