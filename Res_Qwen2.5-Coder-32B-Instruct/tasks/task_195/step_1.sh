echo "Starting the process to find files larger than the average file size."
find . -type f -exec ls -lh {} + | awk '{sum+=$5; n++} END {if (n > 0) print sum/n}'