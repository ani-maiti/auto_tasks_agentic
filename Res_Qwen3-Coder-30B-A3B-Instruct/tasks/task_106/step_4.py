import dns.resolver

try:
    # Query A records for github.com
    answers = dns.resolver.resolve('github.com', 'A')
    
    # Print each IP address
    for ip in answers:
        print(ip.to_text())
        
except Exception as e:
    print(f"Error: {e}")