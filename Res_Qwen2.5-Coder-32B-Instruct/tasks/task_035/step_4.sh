echo "Files larger than the average size of 55.8923 bytes (detailed):"
find . -type f -exec ls -lh {} + | awk '$5 > 55.8923 {print $9, $5}'