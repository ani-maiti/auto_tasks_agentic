echo "Checking if there are any directories with non-ASCII characters..."
find . -type d | grep -P '[^\x00-\x7F]'