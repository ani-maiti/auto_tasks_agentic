read -p "Path: " search_path
find "$search_path" -type l -ls 2>/dev/null | grep "broken"