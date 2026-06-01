echo "Files larger than the average size of 94.4583 bytes:"
find . -type f -exec ls -l {} + | awk '$5 > 94.4583 {print $9}'