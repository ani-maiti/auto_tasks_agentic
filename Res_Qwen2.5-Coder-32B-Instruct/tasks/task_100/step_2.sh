echo "Retrieving SSL certificate expiration date for wikipedia.org..."
openssl s_client -connect wikipedia.org:443 2>/dev/null | openssl x509 -noout -enddate