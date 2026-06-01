echo "Searching for SQLite databases with different extensions..."
find . -type f \( -iname "*.sqlite3" -o -iname "*.sqlitedb" -o -iname "*.sdb" \)