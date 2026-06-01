echo "Searching subdirectories for names longer than 20 characters..."
find . -mindepth 1 -maxdepth 1 -type d -exec bash -c 'for dir; do if [ ${#dir} -gt 20 ]; then echo "$dir"; fi done' _ {} +