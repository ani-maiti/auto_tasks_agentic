echo "Starting to find average file size across the current directory tree."
find . -type f -exec ls -l {} + | awk '{sum += $5; count++} END {print "Total size:", sum, "Number of files:", count}'