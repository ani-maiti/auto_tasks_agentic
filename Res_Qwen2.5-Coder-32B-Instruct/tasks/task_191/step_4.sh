echo "Found $(find . -type f -mtime -1 | wc -l) files modified within the last day."
find . -type f -mtime -1 -print