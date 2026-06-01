echo "Finding the ten newest files in the current directory tree..."
find . -type f -printf "%T+ %p\n" | sort -r | head -n 10