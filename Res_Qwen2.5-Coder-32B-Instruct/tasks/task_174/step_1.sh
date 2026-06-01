echo "Starting search for files containing 'artificial intelligence'..."
find . -type f -exec grep -l "artificial intelligence" {} \;