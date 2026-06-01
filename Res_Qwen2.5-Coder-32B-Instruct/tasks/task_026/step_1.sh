echo "Starting search for files with non-ASCII characters..."
find . -type f | grep -P '[^\x00-\x7F]'