echo "Listing first 10 files modified within the last week"
find . -type f -mtime -7 | head -n 10