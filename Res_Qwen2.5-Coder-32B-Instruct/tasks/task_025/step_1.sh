echo "Starting file size collection..."
find . -type f -exec ls -lh {} + | awk '{print $5, $9}' > file_sizes.txt
echo "File sizes collected."