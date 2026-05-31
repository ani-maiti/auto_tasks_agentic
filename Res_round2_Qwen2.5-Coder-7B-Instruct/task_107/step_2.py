import dns.resolver

hostname = 'wikipedia.org'
try:
    answers = dns.resolver.resolve(hostname, 'A')
    for answer in answers:
        print(f"A record for {hostname}: {answer.address}")
except dns.resolver.NoAnswer:
    print(f"No A records found for {hostname}")
except dns.resolver.NXDOMAIN:
    print(f"{hostname} does not exist")
except Exception as e:
    print(f"An error occurred: {e}")