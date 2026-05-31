echo "The top 100 largest files are:"
cat <<EOF
$(du -ah --max-depth=1 | sort -hr | head -n 100)
EOF