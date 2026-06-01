echo "Starting file size check..."
find . -type f -exec ls -lh {} + | awk '{print $5, $9}' > file_sizes.txt
echo "File sizes saved to file_sizes.txt"