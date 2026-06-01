echo "Starting search for largest Python file..."
find . -type f -name "*.py" -exec ls -lh {} + | awk '{print $5, $9}' | sort -nr | head -n 1