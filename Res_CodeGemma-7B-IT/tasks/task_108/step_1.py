import dns

# Create a DNS resolver object.
resolver = dns.resolver()

# Set the DNS server to Google's public DNS server.
resolver.nameservers = ['8.8.8.8']

# Query the DNS server for the MX records of gmail.com.
mx_records = resolver.query('gmail.com', dns.rdatatype.MX)

# Print the MX records.
for record in mx_records:
    print(record.exchange, record.preference)