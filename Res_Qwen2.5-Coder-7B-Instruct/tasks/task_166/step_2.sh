for file in $(find . -type f); do
    echo "$(stat -c %Y $file) $file"
done | sort -n | head -n 10