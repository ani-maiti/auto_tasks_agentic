read -p "Path to search: " search_path
find "$search_path" -type l -ls 2>&1 | grep "broken"