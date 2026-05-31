import dns.resolver

print("Retrieving MX records for gmail.com...")
mx_records = dns.resolver.resolve('gmail.com', 'MX')
for record in mx_records:
    print(f"MX Record: {record.exchange} with preference {record.preference}")