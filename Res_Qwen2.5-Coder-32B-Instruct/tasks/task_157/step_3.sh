echo "Counting files with uppercase letters in their names:"
find . -type f | grep '[A-Z]' | wc -l