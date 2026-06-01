echo "Starting to gather file sizes..."
find . -type f -exec ls -l {} + | awk '{print $5}'