echo "Average file size is 55.8923 bytes"
find . -type f -exec ls -l {} + | awk '$5 > 55.8923 {print $9}'