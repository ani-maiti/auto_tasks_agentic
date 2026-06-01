while read -r size; do
    grep "^$size " file_sizes.txt | awk '{print $2}' | xargs -I {} basename {} > names_$(echo $size).txt
done < duplicate_sizes.txt
echo "Names of files with duplicate sizes saved to names_*.txt"