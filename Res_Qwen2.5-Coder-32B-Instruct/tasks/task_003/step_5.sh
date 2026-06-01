echo "Detailed list of files modified within the last 24 hours:"
find . -type f -mtime -1 -exec ls -lh {} + | awk '{print $6, $7, $8, $9}'