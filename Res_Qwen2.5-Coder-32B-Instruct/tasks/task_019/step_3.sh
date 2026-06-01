echo "Searching for broken symbolic links in the home directory..."
find ~ -type l -exec test ! -e {} \; -print