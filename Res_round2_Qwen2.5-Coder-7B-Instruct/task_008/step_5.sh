read -p "Enter the path to search for symbolic links: " search_path
find "$search_path" -type l -ls