echo "Retrieving SSL certificate expiration date for wikipedia.org..."
openssl s_client -connect wikipedia.org:443 -servername wikipedia.org 2>/dev/null | openssl x509 -noout -enddate