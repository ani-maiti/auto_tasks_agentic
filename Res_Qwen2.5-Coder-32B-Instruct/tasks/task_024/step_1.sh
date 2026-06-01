echo "Starting search for the oldest file in the current directory tree."
find . -type f -printf "%T+ %p\n" | sort | head -n 1