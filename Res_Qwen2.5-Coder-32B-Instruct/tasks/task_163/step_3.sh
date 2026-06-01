echo "Listing files smaller than 100 bytes..."
find . -type f -size -100c -exec ls -lh {} +