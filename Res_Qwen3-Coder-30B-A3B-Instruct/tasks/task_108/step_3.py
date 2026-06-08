import socket
import dns.resolver

try:
    mx_records = dns.resolver.resolve('gmail.com', 'MX')
    for record in mx_records:
        print(record.exchange)
except Exception as e:
    print(f"Error: {e}")