echo "Starting search for broken symbolic links in the current directory..."
find . -type l -exec test ! -e {} \; -print