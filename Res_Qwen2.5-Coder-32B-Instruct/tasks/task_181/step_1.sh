echo "Starting duplicate file search based on size and name."
find . -type f -printf "%s %p\n" | sort -n > file_sizes.txt
echo "File sizes and paths saved to file_sizes.txt"