echo "Checking if these files contain valid JSON objects..."
for file in $(find . -type f -name "*.json"); do
    if jq empty "$file" > /dev/null 2>&1; then
        echo "$file contains valid JSON"
    else
        echo "$file does not contain valid JSON"
    fi
done