echo "Counting symbolic links in the current directory"
find . -maxdepth 1 -type l | wc -l