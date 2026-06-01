echo "Total number of lines across all .py files:"
find . -name "*.py" -exec cat {} + | wc -l