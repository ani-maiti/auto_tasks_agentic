echo "Counting lines in each shell script..."
for file in $(find . -type f \( -name "*.sh" -o -name "*.bash" \)); do
    echo "$file: $(wc -l < "$file")"
done