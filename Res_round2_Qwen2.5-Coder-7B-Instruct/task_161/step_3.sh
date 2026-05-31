read -p "Enter the path to search: " search_path
find "$search_path" -type d -exec sh -c 'if [ "$(ls -1 "$0" | wc -l)" -gt 100 ]; then echo "$0"; fi' {} \;