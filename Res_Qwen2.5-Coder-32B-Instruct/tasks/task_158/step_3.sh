find . -type f | grep -E '\.[^/]*\.' > files_with_multiple_dots.txt
echo "List of files saved to files_with_multiple_dots.txt"