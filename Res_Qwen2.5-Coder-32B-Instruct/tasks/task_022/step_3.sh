echo "Checking if there are any directories with executable files..."
find . -maxdepth 1 -type d | while read dir; do
    echo "Checking directory: $dir"
    find "$dir" -maxdepth 1 -type f -executable
done