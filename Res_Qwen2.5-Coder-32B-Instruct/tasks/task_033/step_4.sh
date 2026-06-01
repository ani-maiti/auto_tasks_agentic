echo "Identifying files with duplicate sizes..."
while read -r size; do
    grep "^$size" sorted_file_sizes.txt
done < duplicate_sizes.txt > duplicate_files.txt
echo "Files with duplicate sizes saved to duplicate_files.txt"