echo "Listing files modified within the last hour with details:"
find . -type f -mmin -60 -exec ls -lh {} +