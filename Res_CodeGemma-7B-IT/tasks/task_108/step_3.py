import dns.resolver

# Create a DNS resolver object.
resolver = dns.resolver.Resolver()

# Set the DNS server to Google's public DNS server.
resolver.nameservers = ['8.8.8.8']

# Query the DNS server for the MX records of gmail.com.
mx_records = resolver.resolve('gmail.com', dns.rdatatype.MX)

# Print the MX records.
for record in mx_records:
    print(record.exchange, record.preference)
```
execution trace:
stdout:
gmail-smtp-in.l.google.com. 5
alt4.gmail-smtp-in.l.google.com. 40
alt2.gmail-smtp-in.l.google.com. 20
alt1.gmail-smtp-in.l.google.com. 10
alt3.gmail-smtp-in.l.google.com. 30


stderr:
/home/ai_admin/aniruddha/nasa_seed/./tasks/task_108/step_3.py:10: DeprecationWarning: please use dns.resolver.Resolver.resolve() instead
  mx_records = resolver.query('gmail.com', dns.rdatatype.MX)


return code: 0