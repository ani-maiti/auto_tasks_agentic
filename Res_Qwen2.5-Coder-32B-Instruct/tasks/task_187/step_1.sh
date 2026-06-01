echo "Starting search for executable files..."
find . -type f -executable -print0 | xargs -0 ls -lh