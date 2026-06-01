echo "Checking each file for 'import pandas'..."
for file in $(find . -type f -name "*.py"); do
    if grep -q "import pandas" "$file"; then
        echo "Found: $file"
    fi
done