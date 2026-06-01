echo "Finding duplicates..."
awk '{print $1}' sorted_file_sizes.txt | uniq -d > duplicate_sizes.txt
echo "Duplicate sizes saved to duplicate_sizes.txt"