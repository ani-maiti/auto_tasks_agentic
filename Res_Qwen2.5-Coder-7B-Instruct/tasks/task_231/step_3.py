import dns.resolver

# Define the URL of the documentation website
url = "https://docs.example.com"

# Use DNS resolver to find the IP address
try:
    answers = dns.resolver.resolve(url.replace("https://", "").replace("http://", ""), 'A')
    for answer in answers:
        print(f"Resolved IP address: {answer.address}")
except dns.resolver.NoAnswer:
    print(f"No answer found for the domain name.")
except dns.resolver.NXDOMAIN:
    print(f"The domain name does not exist.")
except dns.resolver.Timeout:
    print(f"Timeout while resolving the domain name.")