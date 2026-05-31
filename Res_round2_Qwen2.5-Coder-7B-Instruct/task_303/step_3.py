# Step 3: Use an alternative domain or check network connectivity
alternative_domains = ["data.gov", "open.data.gov"]

for domain in alternative_domains:
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"Alternative domain {domain} resolves to IP address {ip_address}")
        break
    except socket.gaierror:
        continue
else:
    print("None of the alternative domains could be resolved")
    exit(1)