import socket
import dns.resolver

try:
    mx_records = dns.resolver.resolve('gmail.com', 'MX')
    print("MX records for gmail.com:")
    for record in mx_records:
        print(f"  {record.preference} {record.exchange}")
except Exception as e:
    print(f"Error: {e}")