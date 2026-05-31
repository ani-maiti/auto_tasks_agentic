# Check if there are any SQLite databases in the current directory
if [ -z "$(ls *.db 2>/dev/null)" ]; then
    echo "No SQLite databases found in the current directory."
else
    echo "SQLite databases found:"
    ls *.db
fi