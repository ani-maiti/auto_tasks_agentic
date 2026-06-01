echo "Retrieving SSL certificate expiration date for github.com..."
openssl s_client -connect github.com:443 2>/dev/null | openssl x509 -noout -enddate