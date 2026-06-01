echo "Neither dig nor nslookup is installed. Using Python's dns.resolver module."
python3 -c "import dns.resolver; print(dns.resolver.resolve('outlook.com', 'MX'))"