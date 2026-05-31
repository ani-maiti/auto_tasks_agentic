# Check if there are any SQLite database files
if [ ! -s sqlite_databases.txt ]; then
    echo "No SQLite databases found."
else
    grep -E '\.db$' sqlite_databases.txt > sqlite_databases_filtered.txt
fi