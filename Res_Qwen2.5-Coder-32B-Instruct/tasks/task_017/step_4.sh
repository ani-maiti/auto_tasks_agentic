echo "Displaying the 50 most recently modified files in /home directory..."
find /home -type f -printf '%T+ %p\n' 2>/dev/null | sort -r | head -n 50