echo "Counting directories with uppercase letters in their names:"
find . -type d | grep '[A-Z]' | wc -l