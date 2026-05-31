read -p "Enter the path to search: " search_path
find "$search_path" -type d -exec sh -c 'find "{}" -maxdepth 1 -type f | wc -l' \; | awk '$1 > 100 {print $2}'