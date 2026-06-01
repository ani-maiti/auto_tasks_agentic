echo "Retrieving SSL certificate issuer for github.com..."
openssl s_client -connect github.com:443 2>/dev/null | openssl x509 -issuer -noout