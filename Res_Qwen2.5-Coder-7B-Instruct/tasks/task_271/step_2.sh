# Filter out non-SQLite database files
grep -E '\.db$' sqlite_databases.txt > sqlite_databases_filtered.txt