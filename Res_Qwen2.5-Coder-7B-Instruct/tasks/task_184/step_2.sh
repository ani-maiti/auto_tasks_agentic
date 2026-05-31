for file in $(find . -name "*.json"); do
    if jq . "$file" &> /dev/null; then
        echo "File $file is valid JSON."
    else
        echo "File $file is NOT valid JSON."
    fi
done