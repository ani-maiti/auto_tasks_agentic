echo "Starting to find the ten oldest files in the current directory tree."
find . -type f -printf "%T+ %p\n" | sort | head -n 10