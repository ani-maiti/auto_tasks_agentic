import dns.resolver

resolver = dns.resolver.Resolver()

try:
    mx_records = resolver.resolve("outlook.com", dns.rdatatype.MX)
    for record in mx_records:
        print(record.exchange)
except dns.resolver.NoAnswer:
    print("No MX records found for outlook.com")