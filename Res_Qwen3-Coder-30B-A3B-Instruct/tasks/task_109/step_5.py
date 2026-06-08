import dns.resolver

try:
    # Query MX records for outlook.com
    mx_records = dns.resolver.resolve('outlook.com', 'MX')
    
    # Print all MX records with their priorities
    print("MX Records for outlook.com:")
    for record in mx_records:
        print(f"Priority: {record.preference}, Exchange: {record.exchange}")
        
except Exception as e:
    print(f"Error: {e}")