echo "Summing up all comment lines..."
total_comments=0
for file in $(find . -type f -name "*.py"); do
    comments=$(grep -c '^#' "$file")
    total_comments=$((total_comments + comments))
done
echo "Total comment lines: $total_comments"