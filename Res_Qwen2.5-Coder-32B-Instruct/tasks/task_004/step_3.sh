echo "Listing paths for each duplicate filename:"
for file in $(find . -type f -printf "%f\n" | sort | uniq -d); do
    echo "Filename: $file"
    find . -type f -name "$file"
done