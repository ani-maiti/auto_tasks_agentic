echo "Starting search for files containing email addresses..."
find . -type f -exec grep -E -o "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b" {} +