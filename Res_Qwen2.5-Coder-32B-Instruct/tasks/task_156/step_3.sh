echo "Files ending with a digit:"
find . -type f -name '*[0-9]' | grep -E '[0-9]$'