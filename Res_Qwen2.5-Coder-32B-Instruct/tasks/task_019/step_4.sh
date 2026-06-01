echo "Broken symbolic links found in the home directory:"
find ~ -type l -exec test ! -e {} \; -print