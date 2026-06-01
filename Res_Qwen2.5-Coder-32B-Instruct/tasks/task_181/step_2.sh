awk '{print $1}' file_sizes.txt | uniq -d > duplicate_sizes.txt
echo "Duplicate sizes saved to duplicate_sizes.txt"