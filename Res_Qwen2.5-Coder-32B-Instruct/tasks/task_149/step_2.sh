echo "Found Python files. Now counting lines in each file."
for file in $(find . -type f -name "*.py"); do
    echo "$file,$(wc -l < "$file")"
done > python_files_line_counts.csv