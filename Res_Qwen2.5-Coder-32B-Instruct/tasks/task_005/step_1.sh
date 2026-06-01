echo "Starting file size check..."
find . -type f -size +1M -exec ls -lh {} \;