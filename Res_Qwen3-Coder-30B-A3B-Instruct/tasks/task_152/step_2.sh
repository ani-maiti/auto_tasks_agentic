total_comments=0
for file in $(find . -name "*.py" -type f); do
    comments=$(grep -c "^#" "$file")
    total_comments=$((total_comments + comments))
done
echo $total_comments