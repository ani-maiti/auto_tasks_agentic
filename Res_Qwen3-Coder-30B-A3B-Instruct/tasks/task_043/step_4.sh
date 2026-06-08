for file in $(find . -name "*.csv" -type f); do
    echo "File: $file"
    wc -l < "$file"
done