read -p "Enter the path to search for executable files: " search_path
find "$search_path" -type f -executable -exec ls -lh {} + 2>/dev/null