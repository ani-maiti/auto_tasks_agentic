echo "Counting files in each directory..."
for dir in $(find . -type d); do
    count=$(find "$dir" -maxdepth 1 -type f | wc -l)
    if [ "$count" -gt 50 ]; then
        echo "$dir contains $count files"
    fi
done