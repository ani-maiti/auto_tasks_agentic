echo "Starting to find the 50 most recently modified files..."
find / -type f -printf '%T+ %p\n' 2>/dev/null | sort -r | head -n 50