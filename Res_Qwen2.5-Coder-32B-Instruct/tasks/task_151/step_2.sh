echo "Counting blank lines in Python files..."
for file in $(find . -type f -name "*.py"); do
    grep -c '^$' "$file"
done | awk '{sum += $1} END {print sum}'