echo "Counting lines in all shell scripts..."
wc -l $(find . -type f \( -name "*.sh" -o -name "*.bash" \))