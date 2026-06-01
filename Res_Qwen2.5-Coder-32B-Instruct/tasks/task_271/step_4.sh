echo "SQLite databases found:"
cat <<EOF > sqlite_databases.txt
$(find / -type f -name "*.sqlite" -o -name "*.db" 2>/dev/null)
EOF
cat sqlite_databases.txt