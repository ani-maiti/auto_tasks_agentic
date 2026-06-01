import dns.resolver
mx_records = dns.resolver.resolve('outlook.com', 'MX')
for record in mx_records:
    print(record.exchange.to_text(), record.preference)