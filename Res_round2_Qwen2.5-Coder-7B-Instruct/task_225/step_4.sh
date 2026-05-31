# Check if any SQLite databases were found in subdirectories
if [ -z "$(find . -name "*.db" 2>/dev/null)" ]; then
    echo "No SQLite databases found in the current directory or its subdirectories."
else
    echo "SQLite databases found:"
    find . -name "*.db"
fi