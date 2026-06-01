echo "Listing first 10 files modified within the last month"
find . -type f -mtime -30 | head -n 10