echo "Retrieving SSL certificate expiration date for python.org..."
openssl s_client -connect python.org:443 2>/dev/null | openssl x509 -noout -enddate