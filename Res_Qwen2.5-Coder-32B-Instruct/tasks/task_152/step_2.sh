echo "Counting comment lines in each Python file..."
for file in $(find . -type f -name "*.py"); do
    echo "Processing $file"
    grep -c '^#' "$file"
done