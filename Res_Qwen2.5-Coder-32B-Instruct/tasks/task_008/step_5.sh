echo "Listing symbolic links and their targets in the current directory..."
find . -maxdepth 1 -type l -exec ls -l {} + | awk '{print $NF" -> "$11}'