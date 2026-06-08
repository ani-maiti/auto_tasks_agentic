import socket
import dns.resolver

try:
    # Query MX records for outlook.com
    mx_records = dns.resolver.resolve('outlook.com', 'MX')
    
    # Print all MX records
    for record in mx_records:
        print(record.exchange)
        
except Exception as e:
    print(f"Error: {e}")