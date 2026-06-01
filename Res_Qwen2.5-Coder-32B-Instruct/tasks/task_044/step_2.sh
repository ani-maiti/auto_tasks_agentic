echo "Filtering out empty files..."
find . -type f ! -empty -exec ls -l {} + | sort -n -k 5 | head -n 1