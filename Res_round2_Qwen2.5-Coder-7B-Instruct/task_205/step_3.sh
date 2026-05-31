for db in $(cat sqlite_databases.txt); do
    echo "Inspecting $db"
    sqlite3 "$db" ".schema" >> schemas.sql
done