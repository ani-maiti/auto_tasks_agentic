import dns.resolver

domain_name = "github.com"

try:
    resolver = dns.resolver.Resolver()
    answers = resolver.query(domain_name, dns.rdatatype.A)

    for rdata in answers:
        print(rdata.address)
except dns.resolver.NXDOMAIN:
    print("Domain not found")
except Exception as e:
    print(f"Error retrieving IP address: {e}")
```
execution trace:
stdout:
140.82.112.53
140.82.112.204
140.82.112.202
140.82.112.203


stderr:


return code: 0