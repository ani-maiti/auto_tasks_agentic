echo "Files larger than the average size of 55.8923 bytes:"
find . -type f -exec ls -l {} + | awk '$5 > 55.8923 {print $9, $5}'