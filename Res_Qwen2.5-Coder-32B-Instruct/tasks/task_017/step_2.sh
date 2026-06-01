echo "Filtering out /proc entries and searching again..."
find /home -type f -printf '%T+ %p\n' 2>/dev/null | sort -r | head -n 50