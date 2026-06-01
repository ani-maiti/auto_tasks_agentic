echo "Listing symbolic links in the current directory..."
find . -maxdepth 1 -type l -exec ls -l {} \;